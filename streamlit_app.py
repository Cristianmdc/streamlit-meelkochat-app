import streamlit as st
import openai

# Define OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Meelko Pellet Assistant")
st.write("Ask me anything about Meelko Pellet Mills!")

user_input = st.text_input("Your question:")
if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are Meelko Pellet Assistant."},
                      {"role": "user", "content": user_input}]
        )
        st.write(response["choices"][0]["message"]["content"])
    except Exception as e:
        st.error(f"Error: {e}")
