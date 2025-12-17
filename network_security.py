from flask import request, abort
from models import db, AuditLog
import logging

# Trusted IPs for Admin access
ALLOWED_ADMIN_IPS = ["127.0.0.1"]

def ip_check(role):
    """
    Enforces IP-aware network security.
    Restricts Admin access to trusted IP addresses
    and logs denied access attempts.
    """
    ip = request.remote_addr

    if role == "Admin" and ip not in ALLOWED_ADMIN_IPS:
        # Log to application log file
        logging.warning(f"Blocked Admin access attempt from IP: {ip}")

        # Log to database audit table
        log = AuditLog(
            username="Unknown",
            event_type="ACCESS_DENIED",
            ip_address=ip
        )
        db.session.add(log)
        db.session.commit()

        abort(403)
