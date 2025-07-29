import streamlit as st
import google.generativeai as genai


class questionAnswerApplication:
    """Q&A Application module for Streamlit multi-app"""

    def __init__(self):
        """Initialize the Q&A application with API configuration"""
        try:
            self.api_key = st.secrets["GOOGLE_API_KEY"]
            self.system_prompt = st.secrets["qa_system_message"]
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash", 
                system_instruction=self.system_prompt
            )
        except Exception as e:
            st.error(f"Error initializing Q&A application: {e}")
            self.model = None


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
        """Main function to run the Q&A application"""
        st.title("🤖 Q&A Application")
        # st.markdown("Ask a question")
        # File uploader        
        # Text input
        user_input = st.text_input(
            "💬 Enter your query:", 
            placeholder="Ask me anything..."
        )
        
        # Generate response button
        button = st.button("🚀 Ask GenAI", type="primary")
        if button and user_input:
            # Prepare content for the model
            contents = [user_input]
            # Generate and display response
            response_text = self.generate_response(contents)
            if response_text:
                st.markdown("### 📝 Response:")
                st.markdown(response_text)

        elif button and not user_input:
            st.warning("Query missing: Please enter a query before asking GenAI.")


def app():
    """Entry point function for the Q&A application module"""
    qa_app = questionAnswerApplication()
    qa_app.run()


# For testing purposes when run directly
if __name__ == "__main__":
    app()