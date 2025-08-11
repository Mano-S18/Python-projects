# 🛠 My Python Projects Portfolio

A collection of production-ready Python projects showcasing hands-on expertise in **automation**, **data processing**, **web scraping**, **security**, and **file manipulation**.  
Each project was built with clean architecture, error handling, and reusable design in mind.

---

## 📦 Projects

### 1. [🖼 Batch Image Conversion & Smart Thumbnail Generator](Image_processing/)
**Description:**  
A Python-based image automation tool that:
- **Batch converts** images from any format to PNG.
- Creates **sharpened, aspect-ratio-preserving thumbnails** for social media or web use.
- Accepts **source/destination paths** via CLI and dynamically creates output directories.

**Key Learnings:**
- File system navigation (`os`, `pathlib`) and CLI argument parsing.
- Batch processing and automated directory management.
- Image enhancement & resizing using Pillow.

**Tech Stack:** `Python`, `Pillow`, `OS`, `Pathlib`

---

### 2. [📄 Automated PDF Watermarking System](pdf_watermarker/)
**Description:**  
A PDF processing tool that:
- Batch-applies **watermarks** to multi-page PDFs.
- Maintains precise layer control (`over=False` parameter).
- Produces professional-grade output with error handling.

**Key Learnings:**
- Low-level PDF manipulation with `PyPDF2 / pypdf`.
- Binary file I/O and memory-safe operations with context managers.
- Configurable workflows for document branding/security.

**Tech Stack:** `Python`, `PyPDF2 / pypdf`, `Binary I/O`

---

### 3. [📧 Automated HTML Email Sender](Emailing/)
**Description:**  
A secure HTML email automation system that:
- Sends **personalized HTML emails** via Gmail’s SMTP server.
- Uses **TLS encryption** and avoids hard-coded credentials.
- Dynamically injects content into HTML templates.

**Key Learnings:**
- SMTP protocol implementation with `smtplib`.
- HTML templating using `string.Template`.
- MIME-compliant email construction and secure credential handling.

**Tech Stack:** `Python`, `smtplib`, `email`, `pathlib`, `string`

---

### 4. [📰 Hacker News Trend Scraper & Analyzer](Web_scrapping/)
**Description:**  
A web scraping tool that:
- Extracts **trending Hacker News posts** (>100 points).
- Processes multiple pages with **ethical rate limiting**.
- Generates **timestamped JSON reports** for analysis.

**Key Learnings:**
- DOM parsing with BeautifulSoup’s CSS selectors.
- Ethical crawling with `time.sleep()` and `robots.txt` compliance.
- Engagement-based filtering & structured JSON data storage.

**Tech Stack:** `Python`, `BeautifulSoup4`, `Requests`, `JSON`

---

### 5. [🔒 Password Breach Checker with k-Anonymity](Passwordchecker/)
**Description:**  
A security tool that:
- Checks passwords against **613M+ compromised credentials** from Have I Been Pwned.
- Uses **k-Anonymity protocol** to ensure zero password exposure.
- Integrates securely with the HIBP API.

**Key Learnings:**
- SHA-1 hashing with `hashlib` and k-Anonymity principles.
- API integration with secure data handling.
- OWASP-compliant password management.

**Tech Stack:** `Python`, `Requests`, `Hashlib`, `Sys`, `HIBP API`

---

## 📚 What I Learned Across All Projects
- **Automation**: Building tools that save 80–95% manual effort.
- **Security Best Practices**: Secure API usage, credential handling, and OWASP guidelines.
- **Data Processing**: Efficient file handling, batch processing, and structured output.
- **Scalable Design**: Modular architectures for easy maintenance and reuse.
- **Ethical Development**: Rate limiting, respectful scraping, and data privacy compliance.

---

🤝 Contributions
Contributions, issues, and feature requests are welcome!
Feel free to fork and improve any of the tools.
