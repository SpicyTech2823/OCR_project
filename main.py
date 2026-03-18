import streamlit as st
from PIL import Image
import pytesseract
from docx import Document
from io import BytesIO

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Page configuration (logo shown in browser tab and title bar)
st.set_page_config(
    page_title="Khmer OCR",
    page_icon="images/khmerOCR_logo.png",   
    layout="wide",
)

# Header
st.image("images/khmerOCR_logo.png", width=100)
st.title(":blue[Khmer OCR - Extract Text from Images]", text_alignment="center")
st.markdown("Upload an image containing Khmer text, then extract and download as Word document.", text_alignment="center")

# Initialize session state for extracted text
if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button(" Extract Text", type="primary"):
            with st.spinner("Running OCR..."):
                try:
                    text = pytesseract.image_to_string(image, lang='khm')
                    st.session_state.ocr_text = text
                    st.success("OCR completed!")
                except Exception as e:
                    st.error(f"OCR failed: {e}")
    else:
        st.info("Please upload an image to begin.")

with col2:
    st.subheader("2. Extracted Text")
    # Display text area for editing
    edited_text = st.text_area("Review and edit text", 
                                value=st.session_state.ocr_text, 
                                height=300,
                                key="text_editor")
    
    # Update session state if user edits
    if edited_text != st.session_state.ocr_text:
        st.session_state.ocr_text = edited_text
    
    # Download as DOCX
    if st.session_state.ocr_text.strip():
        # Create a Word document in memory
        doc = Document()
        doc.add_paragraph(st.session_state.ocr_text)
        
        # Save to BytesIO
        docx_io = BytesIO()
        doc.save(docx_io)
        docx_io.seek(0)
        
        st.download_button(
            label=" Download as DOCX",
            data=docx_io,
            file_name="extracted_text.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    else:
        st.info("No text extracted yet.")