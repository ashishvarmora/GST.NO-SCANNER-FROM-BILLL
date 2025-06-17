import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import os
import re
import csv

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Optional thresholding for better OCR on tough images
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return pytesseract.image_to_string(gray)

def extract_invoice_no(text):
    pattern = r'(?:Invoice\s*No[:\s]*)(\S+)'
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1) if match else None

def process_all_bills(folder_path):
    results = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = os.path.join(folder_path, file)
            text = extract_text_from_image(full_path)
            invoice_no = extract_invoice_no(text)
            results.append((file, invoice_no))
    return results

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'Invoice No'])
        writer.writerows(data)

if __name__ == "__main__":
    folder = r'C:\Users\15ind\OneDrive\Desktop\CLG prj\python\text from BILL\bill making python\sample_bills'    # Path to the folder containing images
    output_csv = 'extracted_invoice_numbers.csv'

    extracted_data = process_all_bills(folder)
    save_to_csv(extracted_data, output_csv)

    print(f"Done! Extracted data saved to {output_csv}")
