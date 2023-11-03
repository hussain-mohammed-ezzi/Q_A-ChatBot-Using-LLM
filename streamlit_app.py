import os
import streamlit as st
from langchain.llms import GooglePalm 
from dotenv import load_dotenv

load_dotenv() #take environment variable like api

#create  a function to get chatmodel
def get_googlepalm_response(question):
    llm = GooglePalm(google_api_key = os.environ.get('GOOGLE_API_KEY'),temparature = 0.5)
    response = llm(question)
    return response

# intialize the streamlit app 

st.set_page_config(page_title='GooglePalm Q&A Bot ')

st.header('Googlepalm Langchain Application')

question = st.text_input('Type your Question')
response = get_googlepalm_response(question)
submit = st.button('Generate the Answer')

if submit:
    st.subheader('Answer is :')
    st.write(response)