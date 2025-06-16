# Document Analysis Chatbot

This is a Streamlit-based chatbot application that uses Novita AI to analyze and answer questions about your documents. The application supports various file formats including TXT, PDF, DOCX, XLSX, XLS, and CSV files.

## Features

- Document analysis using Novita AI
- Support for multiple file formats (TXT, PDF, DOCX, XLSX, XLS, CSV)
- Interactive chat interface
- Real-time document processing
- Detailed explanations and calculations for data analysis

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Novita AI API key:
   ```
   NOVITA_API_KEY=your_api_key_here
   ```

## Usage

1. Start the application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)
3. In the sidebar, enter the path to your documents folder
4. Click "Initialize Data Source" to load your documents
5. Start asking questions about your documents in the chat interface

## Supported File Types

- Text files (.txt)
- PDF documents (.pdf)
- Word documents (.docx)
- Excel spreadsheets (.xlsx, .xls)
- CSV files (.csv)

