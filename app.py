import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.pdf_loader import extract_text_from_pdf

# Load model
@st.cache_resource
def load_model():
    model_name = "mrm8488/mT5-small-finetuned-tydiqa-for-xqa"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Answer generator
def generate_answer(context, question):
    input_text = f"question: {question} context: {context}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(inputs, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit UI
st.set_page_config(page_title="📖 Telugu PDF Q&A", layout="wide")

st.title("📖 Telugu PDF Question Answering")
st.write("Upload a Telugu PDF, ask questions in Telugu or Romanized Telugu, and get answers!")

uploaded_pdf = st.file_uploader("📄 Upload your Telugu PDF", type=["pdf"])
if uploaded_pdf:
    text = extract_text_from_pdf(uploaded_pdf)
    st.success("✅ PDF uploaded and processed successfully!")

    question = st.text_input("❓ Enter your question (in Telugu or Romanized Telugu):")
    if question:
        with st.spinner("🧠 Thinking..."):
            answer = generate_answer(text, question)
        st.markdown(f"### 📝 Answer:\n> {answer}")
