from dotenv import load_dotenv
load_dotenv() ##loading all the enviourment variables.
import streamlit as st
import google.generativeai as genai
import os
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
##function to get load response from gemini-pro model
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text
#initialize our streamlit app
st.set_page_config(page_title="Q & Ans Demo")
st.header=('Gemini LLM application')
input=st.text_input("Input :", key='Input')
submit=st.button("Ask the question")
##when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The response is :")
    st.write(response)