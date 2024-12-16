import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import T5Tokenizer, T5ForConditionalGeneration
import PyPDF2
import io
import torch

import re
from nltk.tokenize import sent_tokenize

# Download NLTK punkt tokenizer (only needed once)
import nltk
nltk.download('punkt')


st.set_page_config(page_title="AI Proofreader - PDF Proofreader", layout="wide")
# CSS for sticky header and navigation
st.markdown(
    """
    <style>
    /* Styling for the sticky navigation bar */

    /*Added the two css to control the default page behavior a bit*/
    /*.st-emotion-cache-13ln4jf {
        width: 100%;
        padding: 0px; 
        max-width: 46rem;
    }*/

    .main-content {
        width: 100%;
        padding: 1rem; 
        max-width: 75rem;
    }

    #ai-proofreader-pdf-proofreader{
        margin-top: -75px;
    }

    .menu-bar {
        background-color: #f8f9fa;
        padding: 10px;
        margin-top: -110px;
        text-align: right;
        position: -webkit-sticky;
        position: sticky;
        top: 0;
        z-index: 10000000;
        border-bottom: 1px solid #ddd;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    .menu-bar a {
        margin: 0 15px;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        color: #333;
        padding: 8px 15px;
        border-radius: 5px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .menu-bar a:hover {
        background-color: #007BFF;
        color: white;
    }
    .menu-bar a.active {
        background-color: #007BFF;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render the sticky menu bar
query_params = st.query_params
page = query_params.get("page", ["PDF_Proofreader"])[0]

st.markdown(
    f"""
    <div class="menu-bar">
        <a href="Home_Page" class="{ 'active' if page == 'Home_Page' else ''}">Home</a>
        <a href="PDF_Proofreader" class="{ 'active' if page == 'PDF_Proofreader' else ''}">PDF Proofreader</a>
        <a href="Paragraph_Proofreader" class="{ 'active' if page == 'Paragraph_Proofreader' else ''}">Paragraph Proofreader</a>
        <a href="Contact" class="{ 'active' if page == 'contact' else ''}">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)


# Contact Page Content
#st.markdown('<div class="main-content">', unsafe_allow_html=True)





# Use Hugging Face model path directly
MODEL_NAME = "owusuevans14/finetuned_T5_model_for_GEC"

# Load the model and tokenizer from Hugging Face Hub
@st.cache_resource
def load_model_and_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
    return tokenizer, model


def extract_sentences_from_pdf(pdf_file):
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Clean the text (optional: handles edge cases like newlines)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    # Use NLTK's sentence tokenizer for better sentence splitting
    sentences = sent_tokenize(text)
    # Further clean and filter sentences
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences
    return sentences


# Function to process sentences with the model
def process_sentences(sentences, model, tokenizer):
    results = []
    for sentence in sentences:
        inputs = tokenizer(sentence, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(inputs["input_ids"], max_length=512)
        decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if sentence != decoded_output:  # Only add sentences that have been corrected
            results.append({"original": sentence, "corrected": decoded_output})
    return results


# Streamlit UI
st.title("AI Proofreader - PDF Proofreader")

# Upload PDF
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("Processing your PDF...")
    
    # Load the model and tokenizer
    tokenizer, model = load_model_and_tokenizer()
    
    # Extract sentences from the PDF
    sentences = extract_sentences_from_pdf(uploaded_file)
    st.write(f"Extracted {len(sentences)} sentences from the PDF.")
    
    # Process each sentence
    st.write("Correcting sentences...")
    corrections = process_sentences(sentences, model, tokenizer)
    
    # Display results
    if corrections:
        st.write(f"The following {len(corrections)} sentences were corrected:")
        st.write("---")
        for correction in corrections:
            st.write(f"**Original:** {correction['original']}")
            st.write(f"**Corrected:** {correction['corrected']}")
            st.write("---")
    else:
        st.write("No corrections were made. All sentences are grammatically correct!")
else:
    st.write("Please upload a PDF file to begin.")
