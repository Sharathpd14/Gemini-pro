import streamlit as st 
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
def get_response(input,question):
    if input=="":
        response = model.generate_content([input,question])
    else:
        response = model.generate_content(question)
    return response.text



st.set_page_config(page_title="QandA Demo")
st.header("Gemini Application")
input = st.text_input("Input : ",key="input")


upload_file = st.file_uploader("choose a image...",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="uploaded Image",use_column_width=True)
    
    
submit = st.button("Tell me about image")

if submit:
    response = get_response(input,image)
    st.subheader("The response is ")
    st.write(response)
    