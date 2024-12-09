import streamlit as st
import openai

# Set your OpenAI API key securely
openai.api_key = st.secrets["openai_api_key"]

# Streamlit app
st.title("Embedded Chat with GPT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "How can I help you today?"}]

# Display chat messages
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Bot:** {message['content']}")

# User input
user_input = st.text_input("Your message:", key="input")
if user_input:
    # Append user input
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Call GPT API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state["messages"]
    )
    reply = response.choices[0].message["content"]

    # Append bot response
    st.session_state["messages"].append({"role": "assistant", "content": reply})

    # Clear input box
    st.experimental_rerun()
