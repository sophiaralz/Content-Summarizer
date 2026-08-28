import streamlit as st
import requests

st.set_page_config(page_title="AI Study Notes Generator", layout="centered")

st.markdown('''
            <style>
            h1 {
                color: #9B111E !important;
            }
            </style>
        ''', unsafe_allow_html=True)

st.title("AI Content Summarizer & Study Tool")
st.write("Transform YouTube transcripts, articles, or GITHUB READMEs into structured study notes and flashcards")

# user text input
url_input = st.text_input("Paste a URL (YouTube, Article, or GitHub README):")

if st.button("Generate Study Notes", type = "primary"):
    if not url_input:
        st.warning("Please enter a valid URL first")
    else:
        with st.spinner("Processing content and generating your study notes..."):
            try:
                api_url = "http://127.0.0.1:8000/api/summarize"
                response = requests.post(api_url, json ={"url": url_input})

                if response.status_code == 200:
                    data = response.json()
                    st.success("Study notes generated successfully!")
                    st.markdown("---")
                    st.markdown(data["notes"])
                else:
                    error_detail = response.json().get('detail', 'Unknown error')
                    st.error(f"Server Error: {error_detail}")
            
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to FastAPI. Make sure your backend server is running!")