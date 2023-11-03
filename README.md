# Q_A-ChatBot-Using-LLM

We are creating simple Chatbot using GooglePalm LLM model & langchain and Visulaize our application in Streamlit App 

## Prerequisite

- [langchain](https://python.langchain.com/docs/get_started/introduction)
- [streamlit](https://docs.streamlit.io/)



## Create the Environment

    conda create -n <name> python=3.9 -y

## Activate the environment 

    conda activate <name>

## Install the requirements

    pip install -r requirements.txt

## create the googlepalm api key

1. Login you gmail account in 

- [makersuite](https://makersuite.google.com/)


## create the api key and copy paste in your .env file

        GOOGLE_API_KEY = 'enter your api'

## run the app 

        streamlit run app.py