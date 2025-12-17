# Secure IAM System with RBAC and IP-Aware Network Security

A Flask-based Identity and Access Management (IAM) system implementing
Role-Based Access Control (RBAC) with IP-aware network security.

## 🔐 Features
- Secure authentication
- Role-Based Access Control (Admin / Employee)
- IP-based access restriction for Admin
- Audit logging (login success, failure, access denied)
- Admin audit log viewer
- Secure session management

## 🛠 Tech Stack
- Python (Flask)
- SQLite
- Flask-Login
- SQLAlchemy
- HTML / CSS

## 🚀 How to Run Locally
```bash
git clone https://github.com/<your-username>/secure-iam-rbac.git
cd secure-iam-rbac
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
