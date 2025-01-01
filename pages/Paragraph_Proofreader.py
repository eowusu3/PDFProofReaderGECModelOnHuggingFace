import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


# Set Streamlit page configuration
st.set_page_config(page_title="AI Proofreader - Paragraph Proofreader", layout="wide")

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

    #paragraph-sentence-proofreader{
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
        z-index: 100000000;
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
page = query_params.get("page", ["Paragraph_Proofreader"])[0]

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




# Load model and tokenizer with caching
@st.cache_resource
def load_model_and_tokenizer(model_name):
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(torch_device)
    return tokenizer, model, torch_device

# Function to correct a paragraph
def correct_paragraph(paragraph, model, tokenizer, device):
    inputs = tokenizer(paragraph, return_tensors="pt", truncation=True, max_length=512).to(device)
    outputs = model.generate(inputs["input_ids"], max_length=512)
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected

# Streamlit App UI
st.title("Paragraph / Sentence Proofreader")

# Load the model and tokenizer
# Use Hugging Face model path directly
#model_name = "owusuevans14/finetuned_T5_model_for_GEC"
model_name = "deep-learning-analytics/GrammarCorrector"
tokenizer, model, device = load_model_and_tokenizer(model_name)

# Text area for input paragraph
paragraph = st.text_area(
    "Enter a paragraph to proofread:",
    placeholder="Type or paste your paragraph here...",
    height=200
)

# Proofread button
if st.button("Proofread / Correct"):
    if paragraph.strip():  # Ensure input is not empty
        # Correct the paragraph
        corrected_paragraph = correct_paragraph(paragraph, model, tokenizer, device)
        
        # Display the corrected paragraph
        st.subheader("Corrected Paragraph:")
        st.write(corrected_paragraph)
    else:
        st.warning("Please enter a valid paragraph.")