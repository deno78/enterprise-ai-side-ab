# Municipal Facility Booking System - User Manual

## 1. Introduction

This system is a web application for searching, reserving, processing payments, and issuing vouchers for municipal facilities (gymnasiums, meeting rooms, heated pools, etc.).

### How to Start

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.

## 2. Registration and Login

### New Registration
1. Click "Register" in the top navigation
2. Enter username, email, and password (6+ characters)
3. Click "Register"
4. You will be redirected to the login page

### Login
1. Click "Login"
2. Enter your username and password
3. Click "Login"

## 3. Language Settings

Select "日本語", "English", or "中文" from the dropdown in the top-right corner.
Your language preference will be saved for future visits.

## 4. Facility Search

1. Enter keywords in the search box on the home page
2. Filter by type using the dropdown
3. Filter by capacity or maximum price
4. Click "Details" on facility cards for more information

## 5. Availability Check

Select a date on the facility detail page to view time slot availability.
- Green outline: Available
- Gray outline: Unavailable

## 6. Making a Reservation

1. Click "Reserve" on the facility list or detail page
2. Enter date, start time, end time, number of people, and purpose
3. Review the total amount
4. Click "Reserve"
5. You will be redirected to the payment page

## 7. Payment

1. After reservation, the payment page will be displayed
2. Click "Pay Now"
3. A dummy QR code will be displayed
4. Show this QR code at the facility (simulated payment)

## 8. PDF Voucher Download

Click "Download PDF Voucher" on the reservation detail page or payment completion page to download a PDF containing reservation details.

## 9. Reservation List

1. Click "My Reservations" in the top navigation
2. Your reservation list will be displayed
3. Use the "Detail" button to view details, download PDF, or cancel

## 10. Cancelling a Reservation

Click the "Cancel" button on the reservation detail page to cancel your reservation.

## 11. Staff Functions

Accounts with staff role (role=staff) can:
- Add, edit, and delete facility information (Admin > Facilities)
- View all users' reservations (Admin > Reservations)
