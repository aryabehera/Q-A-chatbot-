from dotenv import load_dotenv
load_dotenv() ##loading all the enviourment variables.

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
##function to get load response from gemini-pro model
def get_gemini_response(question):
    model=genai.GenerativeModel("gemini-pro")
    chat=model.start_chat(history=[])
    response=chat.send_message(question,stream=True)
    return response
#initialize our streamlit app
st.set_page_config(page_title="Q & Ans Demo")

st.header=('Gemini LLM application')

#Initialize session_state for chat history does_not exist.
if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []

input=st.text_input("Input :", key="Input")
submit=st.button("Ask the Question")

if submit and input:
    response=get_gemini_response(input)
    ##Add user Query to session chat hsitory
    st.session_state["chat_history"].append(("You",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot",chunk.text))
st.subheader("The Chat history is")

for item in st.session_state['chat_history']:
  try:
    role, text = item 
    st.write(f"{role}: {text}")
  except ValueError:
         print("Skipping item :", item)