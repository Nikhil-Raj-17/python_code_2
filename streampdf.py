import streamlit as st
import PyPDF2
from langchain_groq import ChatGroq





# Initialize ChatGroq instance
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.2,
    groq_api_key="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"
)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

# Function to query the content
def query_pdf_content(pdf_content, query):
    prompt = f"""
    You are a PDF content assistant. The following text is extracted from a PDF document:
    ---
    {pdf_content}
    ---
    Answer the user's query based on the above content. If the answer is not found in the text, reply with 'No information exists.'
    
    Query: {query}
    """
    response = llm.invoke(prompt)
    return response.content.strip()


st.title("📄 PDF Chat Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
pdf_text = extract_text_from_pdf(uploaded_file)


    
query = st.text_input("Ask a question about the PDF:")
if st.button("Get Answer") and query:
    answer = query_pdf_content(pdf_text, query)
    st.write(answer)
