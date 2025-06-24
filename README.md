# Employee-Management-System

# Employee Management System

A Django-based system with REST APIs for managing employee data, departments, attendance, and performance metrics.

## 📌 Project Status

| Task                  | Status      |
|-----------------------|-------------|
| Models                | ✅ Completed |
| Database Setup        | ✅ Completed |
| API Development       | ✅ Completed |
| Authentication        | ✅ Completed |
| Swagger Documentation | ✅ Completed |
| Visualization         | ⏳ Pending   |
| Docker Setup          | ⏳ Pending   |
| Deployment            | ⏳ Pending   |

---

## 🛠️ Technical Stack
- **Backend**: Django 4.x + Django REST Framework
- **Database**: PostgreSQL
- **Auth**: JWT (SimpleJWT)
- **Docs**: Swagger UI (drf-yasg)
- **Visualization**: Chart.js (optional)

---

## ✅ Completed Features

### 1. Models
- **Employee**
  - Name, Email, Phone, Address, Date Joined, Department (FK)
- **Department**
  - Department Name
- **Attendance**
  - Employee (FK), Date, Status (Present/Absent/Late)
- **Performance** 
  - Employee (FK), Rating (1-5), Review Date

### 2. Database
- PostgreSQL configured via `.env`
- Fake data seeding for:
  - 50+ employees
  - 5 departments 
  - 90 days of attendance records
  - Performance reviews

### 3. APIs (DRF)
- **CRUD Endpoints**:
  - `GET/POST/PUT/DELETE /api/employees/`
  - `GET/POST/PUT/DELETE /api/departments/`
  - `GET/POST/PUT/DELETE /api/attendance/`
  - `GET/POST/PUT/DELETE /api/performance/`
- **Features**:
  - JWT Authentication
  - Filtering (department, date ranges)
  - Pagination

### 4. Swagger Docs
- Interactive API explorer at `/swagger/`
- Auto-generated from docstrings
- JWT token support

---

## ⏳ Remaining Tasks

### 1. Visualization (Optional)
- **Charts Needed**:
  ```python
  - Employees per Department (Pie Chart)
  - Monthly Attendance Trends (Bar Chart)