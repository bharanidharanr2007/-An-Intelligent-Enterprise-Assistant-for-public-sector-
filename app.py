import streamlit as st
from chatbot import get_response
from document_processor import extract_text, summarize_document
from profanity_filter import check_profanity

st.title("Enterprise AI Assistant")

user_input = st.text_input("Ask your question")

if user_input:

    if check_profanity(user_input):
        st.warning("Please use professional language.")
    else:
        response = get_response(user_input)
        st.write(response)


uploaded_file = st.file_uploader("Upload Document")

if uploaded_file:

    text = extract_text(uploaded_file)

    if st.button("Summarize Document"):

        summary = summarize_document(text)

        st.write(summary)
