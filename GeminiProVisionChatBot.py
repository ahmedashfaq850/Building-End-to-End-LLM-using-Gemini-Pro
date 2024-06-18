from dotenv import load_dotenv
load_dotenv() #loading all the environment variables from .env file
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

api_key = os.getenv("GOOGLE_API_KEY") # this is how you can access the environment variables

genai.configure(api_key=os.getenv(api_key)) # this is how you load the api key in the generativeai module

# initialize the model
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    
    return response.text


## initialize the streamlit app
st.set_page_config(page_title="Gemini Pro Vision Chatbot")
st.header("Gemini Pro Vision Chatbot")

input = st.text_input("Ask me anything")


upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    
submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image)
    st.write(response)
    
# to run the app, you can use the following command
# streamlit run app.py
