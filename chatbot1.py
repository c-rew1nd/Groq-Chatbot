import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_groq import ChatGroq

# ---------------- CONFIG ----------------
GROQ_API_KEY = "Your_Groq_API_Key_Here"
MODEL_NAME = "llama-3.1-8b-instant"
# ----------------------------------------

st.header("📄 My PDF Chatbot (Groq Powered)")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload your PDF", type="pdf")

# Extract text
if file:
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = text_splitter.split_text(text)

    # Embeddings (HuggingFace)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector store
    vector_store = FAISS.from_texts(chunks, embeddings)

    # User question
    user_question = st.text_input("Ask a question about your document")

    if user_question:
        # Groq LLM
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0.4
        )

        # Retrieval QA
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )

        response = qa_chain.run(user_question)
        st.write(response)







