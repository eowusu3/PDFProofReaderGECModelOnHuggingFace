# import streamlit as st

# st.title("Welcome to AI Proofreader (PDF +) (aka Grammar Correction)")

# st.write("Use the sidebar to navigate between pages.")

# # Add an image with the correct file path
# st.image("proofreading_image.jpg", caption="AI-powered proofreader", use_container_width=True)

import streamlit as st

# Set the Streamlit page configuration to wide layout
st.set_page_config(page_title="AI Proofreader - Homepage", layout="wide")

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

    #welcome-to-ai-proofreader-pdf-aka-grammar-correction{
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
        z-index: 1000000;
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
page = query_params.get("page", ["Home_Page"])[0]

st.markdown(
    f"""
    <div class="menu-bar">
        <a href="Home_Page" class="{ 'active' if page == 'Home_Page' else ''}">Home</a>
        <a href="PDF_Proofreader"  class="{ 'active' if page == 'PDF_Proofreader' else ''}">PDF Proofreader</a>
        <a href="Paragraph_Proofreader"  class="{ 'active' if page == 'Paragraph_Proofreader' else ''}">Paragraph Proofreader</a>
        <a href="Contact"  class="{ 'active' if page == 'contact' else ''}">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)


# Main content padding
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Navigation logic
if page == "Home_Page":
    st.title("Welcome to AI Proofreader (PDF +) (aka Grammar Correction)")
    st.write("Use the navigation bar above to explore the app.")
    st.image("proofreading_image.jpg", caption="AI-powered proofreader", use_container_width=True)

elif page == "PDF_Proofreader":
    st.title("PDF Proofreader")
    st.write("Upload a PDF file for grammar correction.")
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file:
        st.write("Your file has been uploaded.")

elif page == "Paragraph_Proofreader":
    st.title("Paragraph Proofreader")
    st.write("Enter or paste a paragraph for grammar correction.")
    text_input = st.text_area("Enter text here:")
    if st.button("Proofread"):
        st.write("Your corrected paragraph will appear here.")

elif page == "contact":
    st.title("Contact Us")
    st.write("Reach out to us at support@aiproofreader.com.")
    st.write("Follow us on [Twitter](https://twitter.com) or [LinkedIn](https://linkedin.com).")
