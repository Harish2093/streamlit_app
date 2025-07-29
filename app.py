import streamlit as st
from PIL import Image
import sys
import os
import time
from apps.documentProcessing import DocumentProcessingApplication
from apps.questionAnswer import questionAnswerApplication
# Configure page
st.set_page_config(
    page_title="Multi-App Dashboard",
    page_icon="🚀",
    layout="wide"
)

# Add the apps directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
apps_dir = os.path.join(current_dir, 'apps')
if apps_dir not in sys.path:
    sys.path.append(apps_dir)

# Create a sidebar menu
st.sidebar.title("🎯 Application Menu")
st.sidebar.markdown("---")

menu_item = st.sidebar.radio(
    "Choose an option:",
    (
        "🏠 Developer Info",
        "🤖 Q&A Application",
        "📄 Document Processing",
        "✍️ Text Generation",
        "ℹ️ About"
    ),
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("💡 **Tip:** Each application has unique features!")

# Display content based on menu selection
if menu_item == "🏠 Developer Info":
    st.title("👨‍💻 Developer Information")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Hello, I'm Harish! 👋
        
        Welcome to my **Multi-Application Dashboard**! This is a side project where I explore 
        various AI capabilities using Google's Generative AI models.
        
        #### 🌟 What you can do here:
        - **Q&A Application**: Ask questions and upload images for analysis
        - **Text Generation**: Generate creative content
        - **About**: Learn more about the technology stack
        
        #### 🚀 Getting Started:
        Use the sidebar menu to navigate between different applications.
        Each app is designed to showcase different AI capabilities.
        
        ---
        
        **Feedback Welcome!** Feel free to explore and let me know your thoughts.
        """)
    
    with col2:
        st.info("""
        **🔧 Tech Stack:**
        - Streamlit
        - Google Generative AI
        - PIL (Image Processing)
        - Python
        """)

elif menu_item == "🤖 Q&A Application":
    qa_app = questionAnswerApplication()
    qa_app.run()

elif menu_item == "📄 Document Processing":
    try:
        doc_app = DocumentProcessingApplication()
        doc_app.run()
    except ImportError as e:
        st.error(f"❌ Error importing Document processing application: {e}")
        st.info("Please ensure the document_processing.py module is in the apps directory.")
    except Exception as e:
        st.error(f"❌ Error running Document processing application: {e}")

elif menu_item == "✍️ Text Generation":
    st.title("✍️ Text Generation")
    st.info("🚧 This feature is coming soon! Stay tuned for updates.")
    
    # Placeholder for text generation app
    st.markdown("""
    ### What's Coming:
    - Creative writing assistance
    - Content generation
    - Story creation
    - Poetry generation
    """)



elif menu_item == "ℹ️ About":
    st.title("ℹ️ About This Application")
    
    # Get current month and year
    current_month_year = time.strftime("%B %Y")

    st.markdown(f"""
    ### 🎯 Project Overview
    This multi-application dashboard demonstrates various AI capabilities using Google's 
    Generative AI models. It's built with Streamlit for a seamless user experience.
    
    ### 🛠️ Technical Details
    - **Framework**: Streamlit
    - **AI Model**: Google Gemini 1.5 Flash
    - **Image Processing**: PIL (Python Imaging Library)
    - **Architecture**: Modular design with separate app components
    
    ### 📱 Features
    - **Responsive Design**: Works on desktop and mobile
    - **Modular Architecture**: Easy to add new applications
    - **Error Handling**: Robust error management
    - **User-Friendly Interface**: Intuitive navigation
    
    ### 🔐 Privacy & Security
    - API keys are securely managed
    - No data is stored permanently
    - All processing happens in real-time
    
    ---
    
    **Version**: 1.0  
    **Last Updated**: {current_month_year}  
    **Developer**: Harish Patil
    """)
