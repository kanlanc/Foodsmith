# Importing the main function from your backend script
from backend import main_function
import streamlit as st
from PIL import Image
import sys
# sys.path.append('../backend')

# st.title('Image Processor')

# uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
#     st.write("Storing the embeddings for menu items...")
#     image = Image.open(uploaded_file)

#     result = main_function()  # Run your backend main function

#     st.write(result)


# Page Config
st.set_page_config(
    page_title="Image Upload App",
    page_icon="📷",
    layout="wide",
    initial_sidebar_state="expanded",
    theme={
        "primaryColor": "#E694FF",
        "backgroundColor": "#00172B",
        "secondaryBackgroundColor": "#0083B8",
        "textColor": "#DCDCDC",
        "font": "sans-serif"
    },
)

# App Title
st.title("Styled Image Upload App 📷")

# Columns
col1, col2 = st.columns(2)

# Custom CSS for Image Display
custom_css = """
    <style>
        .uploaded-image {
            max-width: 100%;
            height: auto;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Image Upload
with col1:
    st.header("Upload an Image")
    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "png", "jpeg"])

# Image Display
with col2:
    st.header("Preview")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True,
                 channels="RGB", cls="uploaded-image")

# Additional Markdown and HTML Styling
st.markdown("## **Image Analysis Options**")
st.markdown("<hr/>", unsafe_allow_html=True)


# Loading Indicator for Analysis
with st.spinner("Analyzing image..."):
    result = main_function()  # Run your backend main function

    # Simulate image analysis here
    st.success("Analysis complete!")


st.write(result)
