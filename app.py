from dotenv import load_dotenv
load_dotenv() #loading all the environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY") # this is how you can access the environment variables

genai.configure(api_key=os.getenv(api_key)) # this is how you load the api key in the generativeai module