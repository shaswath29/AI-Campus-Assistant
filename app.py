import streamlit as st

st.set_page_config(page_title="AI Campus Assistant")

st.title("AI Campus Assistant 🤖")

st.write("Ask anything about campus life")

question = st.text_input("Your question:")

if question:
    st.write("This is a basic AI assistant response.")
