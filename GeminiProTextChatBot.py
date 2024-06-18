from dotenv import load_dotenv
load_dotenv() #loading all the environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY") # this is how you can access the environment variables

genai.configure(api_key=os.getenv(api_key)) # this is how you load the api key in the generativeai module

# initialize the model
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


## initialize the streamlit app
st.set_page_config(page_title="Gemini Pro Chatbot")
st.header("Gemini Pro Chatbot")

input = st.text_input("Ask me anything")
submit = st.button("Generate Response")

if submit:
    response = get_gemini_response(input)
    st.write(response)
    
# to run the app, you can use the following command
# streamlit run app.py
