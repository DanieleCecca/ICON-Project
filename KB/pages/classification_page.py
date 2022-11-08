import base64
import streamlit as st

# Opening file from file path

file = "classificazione.pdf"

with open(file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Embedding PDF in HTML
pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'    

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)
