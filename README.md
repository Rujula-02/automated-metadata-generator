# **Automated Metadata Generation System (MARS 2025)**

This project presents a user-friendly, web-based system that automatically generates structured metadata from unstructured documents. It supports `.txt`, `.pdf`, and `.docx` formats, and includes **OCR (Optical Character Recognition)** capabilities for scanned image-based documents. Designed with simplicity and accessibility in mind, the system can be run in **Google Colab** and features a clean pastel-themed interface.
---

## 📌 **Project Overview**

As digital content grows, automating metadata generation is essential for organizing, classifying, and retrieving unstructured documents. This system extracts key content and presents it as structured **JSON metadata**, suitable for digital archives, content management systems, and intelligent search applications.
---

## 🔑 **Features**

- **Automated Metadata Extraction**  
  Extracts and generates metadata including:  
  ➤ Title  
  ➤ Word count  
  ➤ Keywords  
  ➤ Summary  
  ➤ Language  
  ➤ File type  
  ➤ Upload time

- **Multi-format Document Support**  
  Accepts `.txt`, `.docx`, `.pdf`, and image-based documents with OCR via Tesseract.

- **Semantic Analysis**  
  Lightweight natural language processing (NLP) techniques are used to identify meaningful keywords and generate summaries.

- **Structured JSON Output**  
  Outputs metadata in clean, machine-readable `.json` format.

- **Web Interface**  
  Simple HTML-based UI with pastel styling to upload files and view results.

- **Google Colab Compatible**  
  Can be run entirely within Google Colab and shared via public links using **ngrok** or **localtunnel**.
---

## 🗂️ **Folder Structure**

automated_metadata/
├── app.py # Flask backend
├── extractor.py # Content extraction logic
├── metadata_generator.py # Metadata generation logic
├── templates/
│ └── index.html # Upload form UI
├── static/
│ └── bg.avif # Background image
├── uploads/ # Runtime folder for uploaded files
├── output/ # Runtime folder for generated metadata
├── MARS.ipynb # Google Colab notebook
├── README.md # Project documentation
└── demo.mp4 / demo_link.txt # Demo video or link

> **Note:** `uploads/` and `output/` folders are created dynamically and should be added to `.gitignore`.
---

## 🚀 **How to Run (Google Colab – Recommended)**

1. Open `MARS.ipynb` in Google Colab.  
2. Run all the cells sequentially.  
3. A public link (via ngrok or localtunnel) will be generated.  
4. Upload any `.txt`, `.pdf`, `.docx`, or image file.  
5. View the extracted metadata and download the `.json` output.
---

## 💻 **Optional: Local Setup**

```bash
git clone https://github.com/YourUsername/MARS_2025.git
cd automated_metadata
pip install -r requirements.txt
python app.py
---

## 📄 **Sample Metadata Output**

```json
{
  "filename": "example.pdf",
  "title": "Fundamentals of Operating Systems",
  "word_count": 1482,
  "keywords": ["operating", "systems", "memory", "scheduling"],
  "summary": "This document introduces the key principles of operating systems...",
  "language": "en",
  "created_time": "2025-06-22T13:40:12",
  "file_type": "application/pdf"
}
---

## 📦 **Deliverables**

- `MARS.ipynb` – Executable Google Colab notebook  
- `app.py`, `extractor.py`, `metadata_generator.py` – Core backend logic  
- `index.html` – Web interface  
- `README.md` – Documentation  
- `demo.mp4` or `demo_link.txt` – Demonstration video or link

