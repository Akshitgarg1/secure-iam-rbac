# ===================== 1. IMPORTS =====================
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, current_user
)
from werkzeug.security import check_password_hash
import logging
import os
from datetime import datetime

from config import Config
from models import db, User, AuditLog
from decorators import role_required
from network_security import ip_check

import pytz
from flask import flash


# ===================== 2. APP SETUP =====================
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# ===================== 3. LOGIN MANAGER =====================
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===================== 4. DATABASE INIT =====================
with app.app_context():
    db.create_all()


# ===================== 5. LOGGING SETUP =====================
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/access.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

@app.before_request
def log_request():
    logging.info(f"{request.remote_addr} accessed {request.path}")


# ===================== 6. ROUTES =====================

@app.route("/")
def home():
    return redirect(url_for("login"))


# ---- Login ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        user = User.query.filter_by(username=username).first()
        ip = request.remote_addr

        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            session["role"] = user.role

            # Update last login info
            user.last_login_ip = ip
            user.last_login_time = datetime.utcnow()

            # Audit log
            db.session.add(AuditLog(
                username=username,
                event_type="LOGIN_SUCCESS",
                ip_address=ip
            ))
            db.session.commit()

            return redirect(url_for("dashboard"))

        # Failed login
        db.session.add(AuditLog(
            username=username,
            event_type="LOGIN_FAILED",
            ip_address=ip
        ))
        db.session.commit()

        flash("Invalid username or password", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


# ---- Logout ----
@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("login"))


# ---- Dashboard ----
@app.route("/dashboard")
@login_required
def dashboard():
    user = User.query.get(current_user.id)

    ist = pytz.timezone("Asia/Kolkata")
    last_login_time = None

    if user.last_login_time:
        last_login_time = user.last_login_time.replace(
            tzinfo=pytz.utc
        ).astimezone(ist)

    return render_template(
        "dashboard.html",
        role=session.get("role"),
        last_login_ip=user.last_login_ip,
        last_login_time=last_login_time
    )


# ---- Admin ----
@app.route("/admin")
@login_required
@role_required("Admin")
def admin():
    ip_check("Admin")
    return render_template("admin.html")


# ---- Employee ----
@app.route("/employee")
@login_required
@role_required("Employee")
def employee():
    user = User.query.get(current_user.id)

    ist = pytz.timezone("Asia/Kolkata")
    last_login_time = None

    if user.last_login_time:
        last_login_time = user.last_login_time.replace(
            tzinfo=pytz.utc
        ).astimezone(ist)

    return render_template(
        "employee.html",
        last_login_ip=user.last_login_ip,
        last_login_time=last_login_time
    )



# ---- Audit Logs ----
@app.route("/audit-logs")
@login_required
@role_required("Admin")
def audit_logs():
    ist = pytz.timezone("Asia/Kolkata")

    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(50).all()

    # Convert timestamps to IST
    for log in logs:
        if log.timestamp:
            log.timestamp = log.timestamp.replace(
                tzinfo=pytz.utc
            ).astimezone(ist)

    return render_template("audit_logs.html", logs=logs)


# ---- Error Handler ----
@app.errorhandler(403)
def access_denied(e):
    return render_template("403.html"), 403


# ===================== 7. RUN APP =====================
if __name__ == "__main__":
    app.run(debug=True)
