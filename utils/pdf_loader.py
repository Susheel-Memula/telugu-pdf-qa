import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
