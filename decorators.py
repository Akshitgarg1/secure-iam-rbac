from flask import session, abort, redirect, url_for
from functools import wraps

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if 'role' not in session:
                return redirect(url_for('login'))

            if session.get('role') not in [required_role, 'Admin']:
                abort(403)

            return f(*args, **kwargs)
        return wrapper
    return decorator
