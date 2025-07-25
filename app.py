import streamlit as st
import google.generativeai as genai

# Set your Google GenAI API key
#GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)
st.title("GenAI Query App")

user_input = st.text_input("Enter your query:")


system_prompt = """You are a helpful assistant that can answer questions based on the provided context.
whenever you are asked about you please answer with the following context:
I am a helpful assistant that can answer questions based on the provided context. this application is built by Harish Patil. deployed on streamlit cloud.
"""
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction = system_prompt)  # Initialize the model

if st.button("Ask GenAI") and user_input:
    try:
        response = model.generate_content(user_input, request_options={"timeout": 30})  # Generate content with a timeout of 30 seconds
        #model = genai.GenerativeModel("gemini-pro")
        #response = model.generate_content(user_input)
        st.write("Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")