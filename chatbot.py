from dotenv import load_dotenv  # function to load environment variables from a .env file into os.environ
import streamlit as st  # Streamlit web app framework; we alias it as 'st' for convenience
from langchain_groq import ChatGroq  # ChatGroq class: adapter to talk to Groq LLM via LangChain-style API
import os  # standard library module for OS interactions (env vars, paths, etc.)

load_dotenv()  # read .env file (if present) and set those values in environment variables

# Configure the Streamlit page appearance and layout
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout = "centered")  # sets title, icon and layout
st.title("Chatbot with Groq LLM 🤖")  # displays a top-level title in the Streamlit app

# Initialize a persistent chat history in Streamlit's session state if it's not already there
if "chat_history" not in st.session_state:  # session_state survives across reruns while the user is active
    st.session_state.chat_history = []  # start with an empty list to store messages as dicts

# Render any existing messages from the chat history to the UI
for message in st.session_state.chat_history:  # iterate over each message dict previously stored
    with st.chat_message(message["role"]):  # open a chat bubble with the message role ('user' or 'assistant')
        st.markdown(message["content"])  # render the plain text (or markdown) content inside the chat bubble

# Create / configure the language model client (does not call the model yet)
llm = ChatGroq(  # instantiate a ChatGroq client to interact with the Groq LLM
    model="llama-3.3-70b-versatile",  # name of the model to use (depends on your Groq account / SDK)
    temperature=0.0,  # sampling temperature: 0.0 -> deterministic / less random responses
)

# Create a chat input box that the user can type into
user_prompt = st.chat_input("Ask me something!")  # returns the text the user submitted (or None if nothing submitted)

if user_prompt:  # this block runs only when the user submits something in the chat input
    st.chat_message("user").markdown(user_prompt)  # immediately show the user's message in the UI
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})  # save the user's message

    # Prepare and send an invocation to the LLM; include a system message and the chat history
    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )  # invoke sends the conversation to the model and returns a response object

    assistant_response = response.content  # extract the text content of the assistant's reply from the response
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})  # store assistant reply

    with st.chat_message("assistant"):  # show the assistant reply in the UI in an assistant-styled bubble
        st.markdown(assistant_response)  # render the assistant's reply (markdown allowed)