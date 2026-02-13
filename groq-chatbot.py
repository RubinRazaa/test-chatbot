import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Llama 3.3 Assistant", page_icon="🤖")
st.title("Chatbot")
st.subheader("Developed by Mohammed Rubin Raza")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! This is a chatbot developed by Mohammed Rubin Raza using LangChain and Llama 3.3. How can I help you today?")
    ]

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("Assistant"):
            st.markdown(message.content)

user_query = st.chat_input("Type your message here...")

if user_query:
    with st.chat_message("Human"):
        st.markdown(user_query)
    
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Assistant"):
        llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
        
        response = llm.invoke(st.session_state.chat_history)
        
        st.markdown(response.content)
        
        st.session_state.chat_history.append(AIMessage(content=response.content))
