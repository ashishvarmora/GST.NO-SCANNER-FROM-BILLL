# 🧾 GST Invoice & GSTIN Scanner (Python Project)

A Python-based tool designed to **scan GST invoices and extract GSTIN numbers, invoice data, and vendor details** using OCR. Includes a **duplicate invoice generator** submodule for testing and validation purposes.
Ideal for finance professionals, auditors, or developers working with GST compliance tools.

---


---

## 🚀 Features

* 🔍 Extract GSTIN, invoice number, date, vendor name from images/PDFs
* 🧠 Uses Tesseract OCR with image preprocessing
* ✅ GSTIN format validation using Regex
* 📄 Exports clean data into CSV format
* 🧪 Dummy invoice generator for testing
* 💡 Can be adapted for mobile/GUI/web interface

---

## 🔧 Technologies Used

* `Python 3.8+`
* `pytesseract` – OCR engine
* `OpenCV` – Image preprocessing
* `reportlab` – For generating dummy GST bills (PDF)
* `re`, `csv`, `os`, `uuid`, `random` – Data handling

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/GST_Invoice_Scanner.git
   cd GST_Invoice_Scanner
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Tesseract OCR is installed on your system:

   * Windows: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
   * Linux: `sudo apt install tesseract-ocr`

---

## ▶️ Usage

### 🧾 Scan Invoices

```bash
python scanner.py --input test_data/sample_invoices/ --output output/extracted_data.csv
```

### 🧪 Generate Test Invoices

```bash
cd DuplicateGenerator
python generate.py --count 5
```

---

## 🧠 Configuration

* Edit `gstin_validator.py` for custom validation rules
* Modify OCR accuracy settings in `ocr_engine.py`
* Change template design in `DuplicateGenerator/templates/`

---

## 🔐 Security

* All processing is done **locally** — no files are uploaded to cloud

---

## 📄 License

MIT License – free to use, distribute, and modify.

---

## ✨ Future Plans

* GUI tool using Tkinter or PyQT
* Upload and scan ZIPs of invoices
* PAN/GSTIN cross-matching
* Excel export with formatting

---

## 👤 Contribution

Contributions welcome! Fork the repo, add features, and open a PR 🚀

---

## 📧 Contact

For bugs, ideas, or help, open an [Issue](https://github.com/your-username/GST_Invoice_Scanner/issues) or message directly.

---

> Built with ❤️ for automation in GST invoice handling.
