## loading all the environment variables
from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
import numpy as np
import pandas as pd

st.markdown("# Simple Chat Bot page 🎈")
st.sidebar.markdown("# Chat Bot page 🎈")

# Replace the google_api_key here
GOOGLE_API_KEY = "******************" #Replace with Google_Api_Key 
genai.configure(api_key=GOOGLE_API_KEY)

## function to load Gemini Pro model and get repsonses
geminiModel=genai.GenerativeModel("gemini-pro") 
chat = geminiModel.start_chat(history=[])
def get_gemini_response(query):
    
    instantResponse=chat.send_message(query,stream=True)
    return instantResponse



st.header("A simple Chat Bot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

inputText=st.text_input("Input: ",key="input")
submitButton=st.button("Get Instant answers")

if submitButton and inputText:
    output=get_gemini_response(inputText)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", inputText))
    st.subheader("The Response is")
    for outputChunk in output:
        st.write(outputChunk.text)
        st.session_state['chat_history'].append(("Bot", outputChunk.text))

        
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")