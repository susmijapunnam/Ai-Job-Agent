import pdfplumber # type: ignore

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_resume_text(pdf_path):
    return extract_text(pdf_path)

def parse_resume(filepath):
    resume_text = extract_resume_text(filepath)
    if not resume_text or len(resume_text.strip()) == 0:
        return "Error: Could not extract readable text from this PDF file. Ensure it is not a scanned image."
    return resume_text
