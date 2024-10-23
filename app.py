import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

dify_api_key = st.secrets["dify_api_key"]
url = "https://api.dify.ai/v1/chat-messages"

st.set_page_config(page_title="Cipher • AI Chatbot")

st.title("Cipher AI • Chatbot")

# Add a description for the chatbot
st.markdown("<p style='font-size: 20px; font-style: italic;'>Welcome to Cipher AI, your intelligent assistant. Ask any question, and I will assist you.</p>", unsafe_allow_html=True)

# Initialize session_state variables
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a greeting message only if this is the first session
if not st.session_state.get("greeting_shown", False):
    greeting = "Hi, how may I help you today?"
    st.session_state.messages.append({"role": "assistant", "content": greeting})
    st.session_state.greeting_shown = True  # Mark greeting as shown

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input
prompt = st.chat_input("Enter your question...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        headers = {
            'Authorization': f'Bearer {dify_api_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "inputs": {},
            "query": prompt,
            "response_mode": "blocking",
            "conversation_id": st.session_state.conversation_id,
            "user": "aianytime",
            "files": []
        }

        with st.spinner("Fetching response..."):
            try:
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                response_data = response.json()

                full_response = response_data.get('answer', '')
                new_conversation_id = response_data.get('conversation_id', st.session_state.conversation_id)
                st.session_state.conversation_id = new_conversation_id

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
                full_response = "An error occurred while fetching the response."

        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Custom message styling
st.markdown(
    """
    <style>
    .stChatMessage-user {
        background-color: #D5DBDB; 
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .stChatMessage-assistant {
        background-color: #E8F8F5; 
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
