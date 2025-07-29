import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
# Set your Google GenAI API key
#GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)
st.title("GenAI Query App")

user_input = st.text_input("Enter your query:")


system_prompt = st.secrets["system_message"]
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction = system_prompt)  # Initialize the model


uploaded_file = st.file_uploader(
    "Attach files (optional):",
    accept_multiple_files=False,
    type=["jpeg", "jpg", "png"]
)

if st.button("Ask GenAI1") and user_input:
    try:
        # Prepare file data if any files are uploaded
        contents = []
        if uploaded_file:
            name = uploaded_file.name
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                st.image(uploaded_file, caption=f"Uploaded {name}", use_container_width=True)
                myfile_content = Image.open(io.BytesIO(uploaded_file.read()))
                contents.append(myfile_content)
            else:
                st.error("Unsupported file type. Please upload a JPEG or PNG image.")
        # Pass files as context if supported by the model
        contents.append(user_input)
        with st.spinner("Generating response..."):
            response = model.generate_content(
                contents,
                request_options={"timeout": 30}
            )
            st.write("Response:")
            st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")