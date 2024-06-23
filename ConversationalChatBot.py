from dotenv import load_dotenv
load_dotenv() #loading all the environment variables from .env file
import os
import streamlit as st
import google.generativeai as genai


my_api_key = os.getenv("GOOGLE_API_KEY") # this is how you can access the environment variables

genai.configure(api_key = my_api_key) # this is how you load the api key in the generativeai module

#initialize the model
model = genai.GenerativeModel("gemini-pro")
# to maintain history
chat = model.start_chat(history=[])

def get_gemini_response(question):
    if question != "":
        response = chat.send_message(question, stream=True)
        return response


st.set_page_config(page_title="Gemini Pro Conversational Chatbot")
st.header("Gemini Pro Conversational Chatbot")
input = st.text_input("Ask me anything")

#Initialize the session state 
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

submit = st.button("Ask the Question")

if submit and input:
    response = get_gemini_response(input)
    ## append the response to the chat history
    st.session_state['chat_history'].append(("You ", input))
    st.subheader('The Response is ')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot ", chunk.text))

# Display the chat history 
st.subheader("Chat History")
for speaker, message in st.session_state['chat_history']:
    st.write(f"{speaker}: {message}")
        
    