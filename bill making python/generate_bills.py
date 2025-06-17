from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os

def generate_sample_bill(invoice_no, date, save_path):
    width, height = 600, 800
    bg_color = (255, 255, 255)
    text_color = (0, 0, 0)

    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font_bold = ImageFont.truetype("arialbd.ttf", 24)
        font_regular = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font_bold = ImageFont.load_default()
        font_regular = ImageFont.load_default()

    # Header
    draw.text((50, 30), "Shree Krishna General Store", fill=text_color, font=font_bold)
    draw.text((50, 80), f"Invoice No: {invoice_no}", fill=text_color, font=font_regular)
    draw.text((50, 110), f"Date: {date}", fill=text_color, font=font_regular)
    draw.text((50, 140), "GSTIN: 27ABCDE1234F1Z5", fill=text_color, font=font_regular)

    draw.line([(50, 170), (550, 170)], fill=text_color, width=2)

    # Table headers
    draw.text((50, 190), "Item", fill=text_color, font=font_bold)
    draw.text((350, 190), "Qty", fill=text_color, font=font_bold)
    draw.text((420, 190), "Price (Rs.)", fill=text_color, font=font_bold)
    draw.text((520, 190), "Total (Rs.)", fill=text_color, font=font_bold)

    # Items to choose from with ranges
    items_list = [
        ("Rice (5kg)", (1, 5), (380, 420)),
        ("Sugar (2kg)", (1, 3), (70, 90)),
        ("Cooking Oil (1L)", (1, 2), (140, 170)),
        ("Salt (1kg)", (2, 5), (25, 35)),
        ("Wheat Flour (2kg)", (1, 4), (90, 120)),
        ("Tea Powder (250g)", (1, 3), (100, 150)),
        ("Milk (1L)", (1, 5), (50, 60))
    ]

    y = 220
    grand_total = 0
    num_items = random.randint(3, 6)  # random number of items per bill

    chosen_items = random.sample(items_list, num_items)
    for item, qty_range, price_range in chosen_items:
        qty = random.randint(*qty_range)
        price = random.uniform(*price_range)
        total_price = qty * price
        grand_total += total_price

        draw.text((50, y), item, fill=text_color, font=font_regular)
        draw.text((360, y), str(qty), fill=text_color, font=font_regular)
        draw.text((430, y), f"{price:.2f}", fill=text_color, font=font_regular)
        draw.text((530, y), f"{total_price:.2f}", fill=text_color, font=font_regular)
        y += 30

    draw.line([(50, y+10), (550, y+10)], fill=text_color, width=2)
    draw.text((400, y + 40), "Grand Total:", fill=text_color, font=font_bold)
    draw.text((530, y + 40), f"Rs.{grand_total:.2f}", fill=text_color, font=font_bold)
    draw.text((50, y + 90), "Thank you for shopping with us!", fill=text_color, font=font_regular)

    # Add noise to simulate scanned bill:
    # 1. Slight blur
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))

    # 2. Add random black dots
    draw = ImageDraw.Draw(img)
    for _ in range(200):  # 200 random noise dots
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        draw.point((x, y), fill=(0,0,0))

    img.save(save_path)


def generate_multiple_bills(folder_path, count=20):
    os.makedirs(folder_path, exist_ok=True)
    for i in range(1, count + 1):
        invoice_no = f"INV202505{i:03d}"
        date = f"{random.randint(10, 28)}-May-2025"
        filename = f"bill_{i}.jpg"
        save_path = os.path.join(folder_path, filename)
        generate_sample_bill(invoice_no, date, save_path)
    print(f"{count} bills generated in folder: {folder_path}")

# Usage example:
generate_multiple_bills("sample_bills", count=20)
