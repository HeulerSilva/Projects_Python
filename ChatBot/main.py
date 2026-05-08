# ChatBot with AI using Streamlit and OpenAI

from groq import Groq
import streamlit as st

#Markdown
st.write("## Chatbot com AI")

text_user = st.chat_input("Digite sua mensagem")