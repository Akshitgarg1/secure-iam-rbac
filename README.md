# 🔐 Secure IAM System  
### Role-Based Access Control (RBAC) + IP-Aware Network Security

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Security](https://img.shields.io/badge/Security-RBAC%20%2B%20IP%20Control-red)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A Flask-based **Identity and Access Management (IAM)** system implementing:

- Role-Based Access Control (RBAC)  
- IP-Aware Network Restrictions  
- Audit Logging & Monitoring  
- Backend-Enforced Authorization  

Designed to demonstrate **enterprise-grade authentication and authorization practices**.

---

## 🎯 Problem Statement

Basic authentication alone is insufficient for secure systems.

Modern applications must ensure:

- Fine-grained role-based permissions  
- Network-aware access control  
- Auditability for compliance  
- Strict backend authorization enforcement  

Without these controls, systems are vulnerable to privilege escalation and unauthorized access.

---

## 💡 Solution Overview

This project implements a secure IAM architecture using Flask where:

- Access control is enforced at the backend  
- UI visibility does NOT imply authorization  
- Admin routes are protected by both RBAC and IP policies  
- All critical security events are logged  

The system clearly demonstrates separation of:

- Authentication  
- Authorization  
- Network validation  
- Monitoring  

---

## 🚀 Key Features

### 🔐 Authentication & Authorization

- Secure session-based login (Flask-Login)
- Role-based access enforcement (Admin / Employee)
- Route protection using custom decorators
- Backend-controlled authorization checks

---

### 🌐 IP-Based Network Security

- Admin routes restricted to allowed IP addresses
- Runtime network validation
- Unauthorized IP access blocked immediately
- Defense-in-depth demonstration

---

### 🧾 Audit Logging & Monitoring

- Login success logging
- Login failure tracking
- Access denied logging
- Timestamped security events
- Admin-only audit viewer
- Last login IP and timestamp tracking (IST conversion)

---

### 🚫 Access Control UX

- Custom 403 Access Denied page
- Role-based feature visibility
- Explicit demonstration that UI ≠ Authorization

---

## 🏗️ System Architecture

```
User Request
     ↓
Authentication (Flask-Login)
     ↓
RBAC Decorator Check
     ↓
IP Network Validation
     ↓
Route Execution
     ↓
Audit Logging
```

All security enforcement is backend-driven.

---

## 🛠 Tech Stack

| Layer | Technologies |
|--------|--------------|
| Backend | Python, Flask |
| Authentication | Flask-Login |
| ORM | SQLAlchemy |
| Database | SQLite (Dev/Demo) |
| Security | RBAC + IP-Based Network Control |
| Frontend | HTML, CSS |
| Deployment | GitHub, Render |

---

## 🖼️ Screenshots

### 🔑 Login Page
![Login](screenshots/login.png)

### 📊 Admin Dashboard
![Admin Dashboard](screenshots/admin.png)

### 👤 Employee Dashboard
![Employee Dashboard](screenshots/employee.png)

### 🚫 403 Access Denied
![403](screenshots/403.png)

### 🧾 Audit Logs
![Audit Logs](screenshots/audit_logs.png)

---

## 🧱 Project Structure

```bash
secure-iam-rbac/
│
├── app.py
├── config.py
├── models.py
├── decorators.py
├── network_security.py
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── admin.html
│   ├── employee.html
│   ├── audit_logs.html
│   └── 403.html
│
├── static/
│   └── css/
│       ├── dashboard.css
│       ├── login.css
│       └── audit_logs.css
│
├── screenshots/
└── README.md
```

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/secure-iam-rbac.git
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

### 4️⃣ Run Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000/login
```

---

## 👤 Default Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Employee | employee | emp123 |

---

## 🔐 Security Principles Demonstrated

- Least Privilege
- Defense in Depth
- Backend-Enforced Authorization
- Auditability & Monitoring
- Secure Session Management
- Network-Aware Privileged Access

---

## 📊 Security Comparison

| Feature | Basic Login System | This IAM System |
|----------|-------------------|----------------|
| Authentication | ✅ | ✅ |
| Role Enforcement | ❌ | ✅ |
| IP Restriction | ❌ | ✅ |
| Audit Logging | ❌ | ✅ |
| Backend Authorization | Partial | Strict |
| Privileged Route Protection | Weak | Strong |

---

## 🚧 Future Enhancements

- Account lockout after failed attempts
- Multi-Factor Authentication (MFA)
- Password reset workflow
- PostgreSQL production database
- Role-permission matrix system
- Audit log filtering & export
- Dockerized deployment
- JWT-based authentication mode

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akshit Garg**  
B.Tech CSE | Security & Backend Enthusiast  

---

⭐ If this project helped you understand secure IAM architecture, consider giving it a star!
