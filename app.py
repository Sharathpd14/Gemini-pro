from dotenv import load_dotenv
load_dotenv() # Loading all the environment variable

import streamlit as st 
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
def get_response(question):
    response = model.generate_content(question)
    return response.text
    
    
st.set_page_config(page_title="QandA Demo")
st.header("Gemini Application")
input = st.text_input("Input : ",key="input")
submit = st.button("Enter")

if submit:
    response=get_response(input)
    st.write(response)