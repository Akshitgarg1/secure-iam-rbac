# 🔐 Secure IAM System with RBAC and IP-Aware Network Security

A Flask-based **Identity and Access Management (IAM)** system implementing **Role-Based Access Control (RBAC)** combined with **IP-aware network security** and **audit logging** to demonstrate enterprise-grade authentication and authorization practices.

---

## 📌 Problem Statement

Modern web applications require more than basic authentication. Without proper authorization controls, network-level restrictions, and auditability, systems are vulnerable to unauthorized access and security breaches. There is a need for a secure IAM solution that:

- Enforces **role-based permissions**
- Restricts privileged access using **network context**
- Maintains **audit trails** for monitoring and compliance
- Clearly separates **visibility and authorization**

---

## 💡 Solution Overview

This project implements a **secure IAM system** using Flask that enforces backend-driven access control through RBAC and IP-based security policies. The system supports multiple user roles (Admin and Employee), logs all authentication and authorization events, and provides a clean, role-aware user interface.

Security enforcement is handled **strictly at the backend**, ensuring that UI visibility does not equate to authorization.

---

## 🛠 Tech Stack

| Layer        | Technologies / Tools |
|-------------|----------------------|
| **Backend** | Python, Flask, Flask-Login, SQLAlchemy |
| **Database** | SQLite (Demo / Development) |
| **Security** | Role-Based Access Control (RBAC), IP-Based Network Access Control, Session-Based Authentication, Audit Logging |
| **Frontend** | HTML, CSS (Custom Styling) |
| **Deployment** | GitHub (Version Control), Render (Cloud Deployment) |

---

## 🚀 Key Features

### 🔐 Authentication & Authorization
- Secure login with session management
- Role-based access enforcement (Admin / Employee)
- Backend-protected routes using decorators

### 🌐 Network Security
- IP-based access restriction for Admin routes
- Unauthorized network access blocked at runtime

### 🧾 Audit Logging
- Logs login success events
- Logs login failure attempts
- Logs access denied events
- Timestamped security records
- Admin-only audit log viewer

### 📊 User Awareness
- Displays last login IP and time
- IST timezone conversion for readability

### 🚫 Access Control UX
- Custom 403 Access Denied page
- Restricted features visible but not accessible (RBAC demonstration)

---

## 🧱 Project Structure

```text
secure-iam-rbac/
│
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── models.py                   # Database models
├── decorators.py               # RBAC decorators
├── network_security.py         # IP-based access checks
├── requirements.txt            # Dependencies
│
├── templates/
│ ├── login.html
│ ├── dashboard.html
│ ├── admin.html
│ ├── employee.html
│ ├── audit_logs.html
│ └── 403.html
│
├── static/
│ └── css/                 # CSS & Assets
│ ├── dashboard.css
│ ├── login.css
│ └── audit_logs.css
│
└── .gitignore             # Files to ignore in Git

``` 
---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/secure-iam-rbac.git
cd secure-iam-rbac
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
python app.py
```

### 5️⃣ Open in Browser

http://127.0.0.1:5000/login

--- 

## 👤 Default Test Credentials

| Role      | Username  | Password  |
|-----------|-----------|-----------|
| Admin     | admin     | admin123  |
| Employee  | employee  | emp123    |

(Credentials can be created via database initialization)

---

## 🔗 Source Code:
```bash
https://github.com/<your-username>/secure-iam-rbac
```
---

## 🎯 Security Principles Demonstrated

- Least Privilege

- Defense in Depth

- Backend-Enforced Authorization

- Auditability & Monitoring

- Secure Session Management

---

## 📈 Future Enhancements :

- Account lockout after repeated failures

- Multi-Factor Authentication (MFA)

- Password reset workflow

- PostgreSQL integration

- Role-permission matrix

- Audit log filtering & export

- Dockerized deployment





