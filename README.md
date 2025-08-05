📄 Telugu PDF QA – Answer in తెలుగు
This is a Streamlit-based web application that allows users to upload a Telugu PDF document and ask questions in English, Telugu script, or Romanized Telugu. The app uses the Hugging Face model mrm8488/mT5-small-finetuned-tydiqa-for-xqa to extract answers based on the provided context from the PDF.


🚀 Features


✅ Upload Telugu-language PDFs.

✅ Ask questions in English, Telugu, or Romanized Telugu.

✅ Get context-aware answers from the uploaded document.

✅ Lightweight, easy to deploy, and open-source.

✅ Completely offline compatible if model is downloaded.



🧠 Model Used


Name: mrm8488/mT5-small-finetuned-tydiqa-for-xqa


Task: Multilingual Question Answering

Supports: Telugu and other languages

Interface: pipeline("text2text-generation") from Hugging Face Transformers



📦 Installation
Make sure you are using Python 3.8–3.11 (not 3.13).

# Clone the repository
git clone https://github.com/your-username/telugu-pdf-qa.git
cd telugu-pdf-qa

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
