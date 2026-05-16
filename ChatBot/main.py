# ChatBot with AI using Streamlit and OpenAI

from groq import Groq
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
model_ia = Groq(api_key=os.getenv('KEY'))

#Markdown
st.write("## Chatbot com AI")

# Streamlit memory
if "list_msg" not in st.session_state:
	st.session_state.list_msg = []

# Show msg
for msg in st.session_state["list_msg"]:
	role = msg["role"]
	content = msg["content"]
	st.chat_message(role).write(content)

text_user = st.chat_input("Digite sua mensagem")

# AI Answer
if text_user:
	st.chat_message("user").write(text_user)
	msg= {"role": "user", "content": text_user}
	st.session_state["list_msg"].append(msg)
	resp_ai = model_ia.chat.completions.create(
		messages=st.session_state["list_msg"],
		model="llama-3.1-8b-instant"
	)

	text_resp_ai = resp_ai.choices[0].message.content

# Show AI msg
	st.chat_message("assistant").write(text_resp_ai)
	msg_ai = {"role": "assistant", "content": text_resp_ai}
	st.session_state["list_msg"].append(msg_ai)

#st.file_uploader("Faça upload de um arquivo", type=["txt", "pdf", "docx"])