# Streamlit UI Generative AI Chatbot
A small Streamlit-based chat UI that demonstrates using the Groq LLM (via the langchain_groq adapter) to build a conversational assistant. The app keeps chat history in Streamlit's session state so conversations persist during a user session.

# Implementation Details
This chatbot app is built using Streamlit for the user interface and the Groq LLM (via the langchain_groq adapter) for generating responses. The main logic is contained in a single Python file, making it easy to understand and extend.

* Environment Setup:
The app uses python-dotenv to load environment variables from a .env file. This is useful for securely storing API keys and configuration settings.

* Streamlit UI:
The app sets up a simple, centered chat interface using Streamlit. The page title and icon are customized for clarity.

* Session-based Chat History:
Chat history is stored in Streamlit’s st.session_state, allowing the conversation to persist across user interactions during a session.

* Message Rendering:
Both user and assistant messages are displayed in chat bubbles. The app loops through the chat history and renders each message with the appropriate role.

* Language Model Integration:
The Groq LLM is accessed via the langchain_groq.ChatGroq class. The model name and temperature are configurable. When the user submits a prompt, the app sends the entire conversation (including a system prompt) to the model and displays the response.

 * Extensibility:
The code is modular and easy to modify. You can change the model, add more features (like file uploads or multi-user support), or customize the UI further.

* Deployment:
The app is deployed and publicly accessible at:
https://genai-chatbot-groq.streamlit.app/
