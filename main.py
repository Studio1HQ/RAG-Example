import streamlit as st
from query_processor import QueryProcessor
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Initialize session state
if 'processor' not in st.session_state:
    st.session_state.processor = None
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Set page config
st.set_page_config(
    page_title="Document Analysis Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("Document Analysis Chatbot")
st.write("Ask questions about your documents!")

# Sidebar for data source configuration
with st.sidebar:
    st.header("Data Source")
    # SQL Database Configuration
    db_user = "root"
    db_password = "qwerty"
    db_host = "localhost"
    db_name = "retail_sales_db"

    # Documents Folder Configuration
    st.subheader("Documents Folder")
    documents_folder = st.text_input(
        "Path to documents folder",
        placeholder="docs"
    )
    
    if st.button("Initialize Data Source"):
        try:
            # Validate and resolve documents folder path
            if not documents_folder:
                st.error("Please provide a documents folder path")
            else:
                # Convert to absolute path
                abs_documents_folder = os.path.abspath(documents_folder)
                if not os.path.exists(abs_documents_folder):
                    st.error(f"Documents folder not found: {abs_documents_folder}")
                elif not os.path.isdir(abs_documents_folder):
                    st.error(f"Path is not a directory: {abs_documents_folder}")
                else:
                    # Initialize query processor with a dummy SQL engine
                     # Create SQL engine
                    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
                    sql_engine = create_engine(connection_string)
                    st.session_state.processor = QueryProcessor(abs_documents_folder, sql_engine)
                    st.success("Data source initialized successfully!")
        except Exception as e:
            st.error(f"Error initializing data source: {str(e)}")

# Main chat interface
st.header("Chat Interface")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your documents"):
    if st.session_state.processor is None:
        st.error("Please initialize data source first!")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        # Process query
        try:
            response = st.session_state.processor.process_query(prompt)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response)
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
