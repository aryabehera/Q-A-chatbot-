from dotenv import load_dotenv
load_dotenv() ##loading all the enviourment variables.
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
 try:
    if input!="":
      response=model.generate_content([input,image])
    else:
       response=model.generate_content(image)
    return response.text 
 except Exception as e:
    st.error(f"Error: {e}")
    return None

st.set_page_config(page_title="Gemini image extractor")
st.header=('Gemini application')
input=st.text_input("Input Prompt:", key='Input')
st.title("Image Upload Example")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg","png"])
image = None
if uploaded_file is not None:
      image = Image.open(uploaded_file)
      st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    
submit=st.button("Tell me about the image")
##if submit is clicked
if submit:
   response=get_gemini_response(input,image)
   if response is not None:
     st.subheader("The response is")
     st.write(response)
