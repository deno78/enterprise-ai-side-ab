# Municipal Facility Booking System - Specifications

## 1. System Overview

A system that allows citizens to search and book municipal facilities (gymnasiums, meeting rooms, heated pools, etc.) using a common account, with simulated payment and PDF voucher output.

## 2. Target Users

### Citizen Users
- Search facilities via smartphone or PC
- Make reservations for selected facilities
- Download PDF vouchers to present when using facilities

### Municipal Staff
- Streamline facility management and reservation operations
- Maintain facility information
- View reservation status and communicate with facility managers

## 3. Feature List

### 3.1 User Management
- User registration (username, email, password, display name)
- Login/Logout (session management)
- Profile editing (display name, email, language settings)
- Role management (citizen / staff)

### 3.2 Facility Search
- Free-text search by facility name and location
- Type filtering (Gymnasium / Meeting Room / Heated Pool)
- Price range specification
- Capacity specification
- Multi-language support (Japanese/English/Chinese)

### 3.3 Reservation Function
- Input reservation date, time, number of people, purpose
- Availability check (time slot display)
- Reservation confirmation (duplicate check)
- Reservation modification
- Reservation cancellation

### 3.4 Simulated Payment
- Dummy QR code generation
- Payment status management

### 3.5 Voucher Output
- PDF format voucher download
- Includes reservation ID, facility name, date/time, number of people

### 3.6 Admin Functions (Staff)
- Add, edit, delete facility information
- View reservation status list

## 4. Technology Stack

| Item | Technology |
|---|---|
| Frontend | Vue.js 3 (CDN) |
| CSS | Bootstrap 5 (CDN) |
| Backend | Python Flask 3.0 |
| Database | SQLite (Flask-SQLAlchemy) |
| PDF Generation | ReportLab |
| QR Code | qrcode + Pillow |
| Authentication | Flask-Login + Flask-Bcrypt |
| Multi-language | vue-i18n (frontend) / model fields (backend) |

## 5. API Endpoints

| Method | Path | Description |
|---|---|---|
| POST | /api/auth/register | User registration |
| POST | /api/auth/login | Login |
| POST | /api/auth/logout | Logout |
| GET | /api/auth/me | Current user info |
| PUT | /api/auth/profile | Update profile |
| GET | /api/facilities | Facility list/search |
| GET | /api/facilities/:id | Facility detail |
| GET | /api/facilities/:id/availability | Availability check |
| POST | /api/facilities | Add facility (staff) |
| PUT | /api/facilities/:id | Update facility (staff) |
| DELETE | /api/facilities/:id | Delete facility (staff) |
| GET | /api/reservations | Reservation list |
| POST | /api/reservations | Create reservation |
| GET | /api/reservations/:id | Reservation detail |
| PUT | /api/reservations/:id | Modify reservation |
| DELETE | /api/reservations/:id | Cancel reservation |
| GET | /api/reservations/:id/pdf | Voucher PDF |
| POST | /api/payments/:id/pay | Process payment |
| GET | /api/payments/:id | Payment status |

## 6. Database

- 5 tables: users, facilities, reservations, payments, reservation_logs
- Detailed schema: see docs/architecture/02_database_schema.md

## 7. Screen List

| Screen | Route | Description |
|---|---|---|
| Facility List | / | Search and listing |
| Facility Detail | /facility?id= | Details and availability |
| Reservation Form | /reserve?id= | Reservation input |
| Payment | /payment?id= | QR code display |
| Reservation List | /reservations | User's reservations |
| Reservation Detail | /reservation?id= | Details, PDF DL, cancel |
| Login | /login | Login form |
| Register | /register | Registration form |
| Profile | /profile | Profile editing |
| Admin Facilities | /admin/facilities | Facility CRUD (staff) |
| Admin Reservations | /admin/reservations | Reservation list (staff) |
