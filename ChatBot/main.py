# ChatBot with AI using Streamlit and OpenAI

from groq import Groq
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
model_ia = Groq(api_key=os.getenv('KEY'))

text_user = st.chat_input("Digite sua mensagem")