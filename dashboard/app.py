import streamlit as st
from src.pipeline import run_pipeline

st.title("Automated News Summarizer")

url = st.text_input("Enter News URL")

if st.button("Generate Summary"):

    title, article, entities, summary = run_pipeline(url)

    st.subheader("Title")
    st.write(title)

    st.subheader("Original Article")
    st.write(article)

    st.subheader("Generated Summary")
    st.write(summary)

    st.subheader("Named Entities")
    st.write(entities)