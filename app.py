import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import fitz  # PyMuPDF
import os

# Set page config
st.set_page_config(page_title="Telugu PDF QA – Answer in తెలుగు", page_icon="📄")

st.title("📄 Telugu PDF QA – Answer in తెలుగు")
st.markdown("Upload your Telugu PDF and ask questions in Telugu (script or Romanized) or English.")

# Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "mrm8488/mT5-small-finetuned-tydiqa-for-xqa"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

qa_pipeline = load_model()

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Upload PDF
uploaded_pdf = st.file_uploader("Upload your Telugu PDF", type="pdf")

# Session state to store extracted text
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

if uploaded_pdf:
    try:
        text = extract_text_from_pdf(uploaded_pdf)
        st.session_state.pdf_text = text
        st.success("✅ PDF Text Extracted Successfully!")
    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")

# Chat input
question = st.chat_input("Ask in English, Telugu, or Romanized Telugu...")

if question:
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        if not st.session_state.pdf_text.strip():
            st.warning("Please upload a valid PDF first.")
        else:
            context = st.session_state.pdf_text
            prompt = f"question: {question} context: {context}"

            with st.spinner("Thinking..."):
                try:
                    result = qa_pipeline(prompt, max_new_tokens=256)[0]["generated_text"]
                except Exception as e:
                    result = f"❌ Model error: {str(e)}"

            if len(result.strip()) < 20:
                result = "ఈ ప్రశ్నకు సంబంధిత సమాచారం PDF లో లేదు. స్పష్టంగా అడగండి లేదా వేరే ప్రశ్న ప్రయత్నించండి."

            st.markdown(result)
