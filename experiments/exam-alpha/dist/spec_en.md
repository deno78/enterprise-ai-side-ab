# Municipal Facility Reservation System Specification

## 1. System Overview

A system that allows citizens to search and reserve municipal facilities (gyms, meeting rooms, heated pools, etc.) using a common account, with mock payment and PDF reservation slip output.

## 2. Target Users

### Citizen Users
- Search facilities via smartphone or PC
- Make reservations for found facilities
- Download PDF reservation slips to show when using facilities

### Municipal Staff
- Streamline facility management and reservation operations
- Maintain facility information
- View reservation status and communicate with facility managers

## 3. Functional Requirements

### 3.1 Facility Search
- Search by facility name, location, type (gym, meeting room, pool, etc.), price, availability

### 3.2 Reservation Function
- Input reservation date/time, number of people, purpose
- Check availability and confirm reservation

### 3.3 Mock Payment Function
- Display dummy payment QR code

### 3.4 Reservation Slip Output
- Output reservation slip in PDF format

### 3.5 Reservation Confirmation/Change/Cancellation
- View list of reservations
- View reservation details
- Cancel reservations

### 3.6 User Management
- User registration, login, logout
- Profile management (name, email, language settings, password change)

## 4. Technology Stack

- Frontend: Vue.js 3 (via CDN)
- Backend: Python Flask
- Database: SQLite
- PDF Generation: fpdf2
- QR Code Generation: qrcode + Pillow

## 5. System Architecture

Single Flask server handling both frontend and backend.

- `app.py`: Main application (API endpoints, authentication, PDF generation)
- `models.py`: Database model definitions
- `templates/index.html`: Vue.js SPA template
- `static/css/style.css`: Stylesheet

## 6. Database Design

### users Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | VARCHAR(80) | Username (unique) |
| email | VARCHAR(120) | Email (unique) |
| password_hash | VARCHAR(256) | Password hash |
| name | VARCHAR(100) | Display name |
| lang | VARCHAR(10) | Language setting (ja/en/zh) |
| created_at | DATETIME | Creation timestamp |

### facilities Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name_ja/en/zh | VARCHAR(200) | Facility name (multilingual) |
| type | VARCHAR(50) | Type (gym/meeting_room/pool) |
| location_ja/en/zh | VARCHAR(200) | Location (multilingual) |
| price | INTEGER | Price (JPY/hour) |
| capacity | INTEGER | Capacity |
| description_ja/en/zh | TEXT | Description (multilingual) |
| created_at | DATETIME | Creation timestamp |

### reservations Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| user_id | INTEGER | User ID (foreign key) |
| facility_id | INTEGER | Facility ID (foreign key) |
| date | DATE | Reservation date |
| start_time | VARCHAR(5) | Start time (HH:MM) |
| end_time | VARCHAR(5) | End time (HH:MM) |
| num_people | INTEGER | Number of people |
| purpose | VARCHAR(500) | Purpose |
| status | VARCHAR(20) | Status (confirmed/cancelled) |
| payment_status | VARCHAR(20) | Payment status (unpaid/paid) |
| created_at | DATETIME | Creation timestamp |

## 7. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | User registration |
| POST | /api/auth/login | Login |
| POST | /api/auth/logout | Logout |
| GET | /api/user | Get user info |
| PUT | /api/user | Update user info |
| GET | /api/facilities | List/search facilities |
| GET | /api/facilities/:id | Facility detail |
| GET | /api/facilities/:id/availability | Check availability |
| GET | /api/reservations | List reservations |
| POST | /api/reservations | Create reservation |
| GET | /api/reservations/:id | Reservation detail |
| PUT | /api/reservations/:id | Update reservation |
| DELETE | /api/reservations/:id | Cancel reservation |
| GET | /api/reservations/:id/payment | Get payment info |
| POST | /api/reservations/:id/payment | Process payment |
| GET | /api/reservations/:id/payment/qr | Get QR code |
| GET | /api/reservations/:id/pdf | Download PDF |
| GET | /api/translations/:lang | Get translations |

## 8. UI/UX Requirements

- Simple and intuitive operation
- Multi-language support (Japanese, English, Chinese) - switchable via header select
- Accessibility support (proper labels, keyboard navigation)
- Responsive design (mobile and PC support)

## 9. Extensibility

- Facility data managed in database, designed for add/edit via admin interface
- Multilingual data structure allows easy addition of new languages
- RESTful API design enables use from mobile apps
