import os
import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas

# Load student data
data = pd.read_csv("student_data.csv")

# Create folders
os.makedirs("output", exist_ok=True)
os.makedirs("pdf", exist_ok=True)

# Load logo
college_logo = Image.open("college_logo.png").convert("RGBA")
college_logo = college_logo.resize((80, 80))

# Fonts
font_large = ImageFont.truetype("arialbd.ttf", 22)
font_medium = ImageFont.truetype("arial.ttf", 16)

# Generate ID cards
for index, row in data.iterrows():
    name = row["Name"]
    regno = row["RegNo"]
    dept = row["Department"]
    year = row["Year"]
    college = row["College"]
    phone = row["Phone"]

    # Create QR Code
    qr_data = f"{name} | {regno} | {dept} | {year} | {phone}"
    qr = qrcode.make(qr_data)
    qr = qr.resize((100, 100))

    # Create blank ID card
    card = Image.new("RGB", (600, 250), "white")
    draw = ImageDraw.Draw(card)

    # Header background
    draw.rectangle([(0, 0), (600, 60)], fill=(0, 102, 204))
    draw.text((20, 15), college, fill="white", font=font_large)
    card.paste(college_logo, (500, 10), college_logo)

    # Student details
    draw.text((20, 80), f"Name   : {name}", fill="black", font=font_medium)
    draw.text((20, 110), f"Reg No : {regno}", fill="black", font=font_medium)
    draw.text((20, 140), f"Dept   : {dept}", fill="black", font=font_medium)
    draw.text((20, 170), f"Year   : {year}", fill="black", font=font_medium)
    draw.text((20, 200), f"Phone  : {phone}", fill="black", font=font_medium)

    # Paste QR code
    card.paste(qr, (470, 130))

    # Paste student photo if available only for 111924CS01128
    if regno == "111924CS01128":
        photo_path = f"{regno}.jpg"
        if os.path.exists(photo_path):
            try:
                photo = Image.open(photo_path).resize((100, 100))
                card.paste(photo, (350, 70))
            except Exception as e:
                print(f"Error loading photo: {e}")
        else:
            print(f"Photo not found for {regno}")

    # Save as PNG
    png_path = f"output/{regno}_id_card.png"
    card.save(png_path)

    # Export to PDF
    pdf_path = f"pdf/{regno}_id_card.pdf"
    pdf = canvas.Canvas(pdf_path, pagesize=(600, 250))
    pdf.drawImage(png_path, 0, 0, width=600, height=250)
    pdf.save()

    print(f"ID card created for {regno} ")

print("\n All ID cards generated successfully!")
