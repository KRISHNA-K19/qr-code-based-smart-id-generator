# QR Code-Based Smart Student ID Generator

A Python app that automatically creates colorful student ID-cards from a CSV file.  
Each card embeds a QR code, college logo, optional student photo, and exports to PNG & PDF.

## Features
- Reads student data (name, reg no, department, year, phone) from **`student_data.csv`**
- Generates "QR codes" with student details ('qrcode')
- Adds college logo and themed header ('Pillow')
- Optionally inserts a student photo for specific Reg Nos
- Exports every card as PNG + PDF ('reportlab')
- Simple to customise colours, fonts, or layout

## Tech Stack
| Tool / Library | Purpose |
| -------------- | ------- |
| Python 3.10    | Core language |
| pandas         | Load & iterate CSV rows |
| Pillow (PIL)   | Build card image, draw text/paste images |
| qrcode         | QR code generation |
| reportlab      | PDF export |
