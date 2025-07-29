import streamlit as st
import google.generativeai as genai
from PIL import Image
import io


class DocumentProcessingApplication:
    """Document Processing Application module for Streamlit multi-app"""

    def __init__(self):
        """Initialize the Document Processing application with API configuration"""
        try:
            self.api_key = st.secrets["GOOGLE_API_KEY"]
            self.system_prompt = st.secrets["document_processing_system_message"]
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash", 
                system_instruction=self.system_prompt
            )
        except Exception as e:
            st.error(f"Error initializing document processing application: {e}")
            self.model = None

    def process_uploaded_file(self, uploaded_file):
        """Process uploaded image file and return PIL Image object"""
        if not uploaded_file:
            return None
            
        try:
            name = uploaded_file.name
            if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                st.image(uploaded_file, caption=f"Uploaded {name}", use_container_width=True)
                # Reset file pointer to beginning
                uploaded_file.seek(0)
                #if name.lower().endswith(".pdf"):
                #    file_content = uploaded_file.read()
                #else:
                file_content = Image.open(io.BytesIO(uploaded_file.read()))
                return file_content
            else:
                st.error("Unsupported file type. Please upload a JPEG or PNG image.")
                return None
        except Exception as e:
            st.error(f"Error processing uploaded file: {e}")
            return None

    def generate_response(self, contents):
        """Generate response using the GenAI model"""
        if not self.model:
            st.error("Model not initialized. Please check your API configuration.")
            return None
            
        try:
            with st.spinner("Generating response..."):
                response = self.model.generate_content(
                    contents,
                    request_options={"timeout": 30}
                )
                return response.text
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return None

    def run(self):
        """Main function to run the document processing application"""
        st.title("🤖 Document Processing Application")
        st.markdown("Upload images and ask questions about them.")

        # File uploader
        uploaded_file = st.file_uploader(
            "📎 Attach a Document",
            accept_multiple_files=False,
            type=["jpeg", "jpg", "png"],
            help="Upload JPEG, PNG image for analysis"
        )
        
        # Text input
        user_input = st.text_input(
            "💬 Enter your query:", 
            placeholder="Ask me anything..."
        )
        
        # Generate response button
        button = st.button("🚀 Ask GenAI", type="primary")
        if button and user_input:
            # Prepare content for the model
            contents = []
            
            # Process uploaded file if exists
            if uploaded_file:
                processed_image = self.process_uploaded_file(uploaded_file)
                if processed_image:
                    contents.append(processed_image)
            else:
                st.warning("No file uploaded. please upload an image or document.")
            
            # Add user input
            contents.append(user_input)
            
            # Generate and display response
            response_text = self.generate_response(contents)
            if response_text:
                st.markdown("### 📝 Response:")
                st.markdown(response_text)

        elif button and not uploaded_file:
            st.warning("Document missing: upload a document before asking GenAI.")

        elif button and not user_input:
            st.warning("Query missing: Please enter a query before asking GenAI.")


def app():
    """Entry point function for the Document Processing application module"""
    doc_app = DocumentProcessingApplication()
    doc_app.run()


# For testing purposes when run directly
if __name__ == "__main__":
    app()