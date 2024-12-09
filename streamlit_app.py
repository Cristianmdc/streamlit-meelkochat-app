import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Function to interact with GPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT model
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app interface
st.title("GPT-Powered App")
st.text("Ask GPT a question!")

user_input = st.text_input("Your Input:")
if user_input:
    output = chat_with_gpt(user_input)
    st.write(output)
