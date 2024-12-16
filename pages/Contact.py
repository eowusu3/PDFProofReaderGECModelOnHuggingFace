import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="AI Proofreader - Contact Us", layout="wide")

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

    #contact-us{
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
page = query_params.get("page", ["Contact"])[0]

st.markdown(
    f"""
    <div class="menu-bar">
        <a href="Home_Page" class="{ 'active' if page == 'Home_Page' else ''}">Home</a>
        <a href="PDF_Proofreader" class="{ 'active' if page == 'PDF_Proofreader' else ''}">PDF Proofreader</a>
        <a href="Paragraph_Proofreader" class="{ 'active' if page == 'Paragraph_Proofreader' else ''}">Paragraph Proofreader</a>
        <a href="Contact" class="{ 'active' if page == 'Contact' else ''}">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)


# Contact Page Content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.title("Contact Us")
st.write("We’d love to hear from you! Please fill out the form below or reach out to us via email or social media.")
st.write("Please call us at: +1 917422946. You can also email us at: owusuevans14@gmail.com")

# Contact Form
with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="Enter your full name")
    email = st.text_input("Your Email", placeholder="Enter your email address")
    subject = st.text_input("Subject", placeholder="Enter the subject of your message")
    message = st.text_area("Message", placeholder="Write your message here...")
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            st.success(f"Thank you {name}! Your message has been sent successfully.")
        else:
            st.error("Please fill out all the required fields.")

# Social Media Links
st.markdown(
    """
    <div class="social-links">
        <h3>Follow Us</h3>
        <a href="https://twitter.com" target="_blank">Twitter</a> |
        <a href="https://linkedin.com" target="_blank">LinkedIn</a> |
        <a href="https://facebook.com" target="_blank">Facebook</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
