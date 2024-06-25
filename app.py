import streamlit as st
import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() #load the env variables
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
##function to load gemini modela in order to get response

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.txt

#intitalise streamlit 


st.set_page_config(page_title="Q&A Demo")
st.header("CalDoc")
input=st.text_input("Input: ", key="input")
submit=st.button("ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("the response is")
    st.write(response)
