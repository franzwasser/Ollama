"""import asyncio
import streamlit as st
from test_ollama import agent

async def ask_agent(message: str) -> str:
    response = await agent.run(message)
    return str(response)

st.set_page_config(
    page_title="Document Agent",
    layout="centered",
)

st.title("Document Agent")
st.caption("Ask a question about the documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Ask a question...")

if user_message:
    
def input_panel():
    st.title("Input Panel")
    st.text_input("Input")
    st.write(" ")
    st.button("Submit")
"""