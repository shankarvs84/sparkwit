import streamlit as st

st.set_page_config(page_title="ESG Survey Automation", page_icon="🎯")
st.header("Welcome to ESG Survey Automation Platform")
st.page_link("pages/chat_with_ESG_survey_GPT.py", label="Chat with ESG survey GPT", icon="🤖")
st.page_link("pages/load_training_data.py", label="Upload training data", icon="📤")
st.page_link("pages/upload_questionnaire.py", label="Upload PDF Questionnaire", icon="🗒️")
