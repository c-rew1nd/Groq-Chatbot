# 📄 PDF Chatbot using Groq + LangChain + Streamlit

This project is a **PDF Question-Answering Chatbot** built using **Streamlit**, **LangChain**, **FAISS**, and **Groq LLMs**.  
Users can upload a PDF and ask questions, and the chatbot will answer based only on the document content.

---

## 🚀 Features

- Upload any PDF file  
- Automatically extracts and chunks text  
- Semantic search using FAISS vector database  
- Fast and accurate answers powered by **Groq (LLaMA 3)**  
- Simple Streamlit UI  

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – UI
- **LangChain** – LLM orchestration
- **Groq API** – Large Language Model
- **FAISS** – Vector similarity search
- **HuggingFace Embeddings**
- **PyPDF2** – PDF text extraction

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/pdf-chatbot-groq.git
cd pdf-chatbot-groq
````

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/binactivate   # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install streamlit langchain langchain-community langchain-groq faiss-cpu sentence-transformers pypdf
```

---

## 🔑 Setup Groq API Key

Get your API key from:
👉 [https://console.groq.com](https://console.groq.com)

In your code, replace:

```python
GROQ_API_KEY = "your_groq_api_key_here"
```

> 💡 Recommended: use environment variables for security.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## 🧠 How It Works

1. User uploads a PDF
2. Text is extracted from the PDF
3. Text is split into chunks
4. Chunks are converted into embeddings
5. FAISS stores embeddings for similarity search
6. Groq LLM answers questions using retrieved chunks

---

## 🤖 Model Used

* **llama3-8b-8192** (Groq)

You can switch to other Groq-supported models if needed.

---

## 📁 Project Structure

```
├── app.py
├── README.md
└── requirements.txt
```

---

## 🔮 Future Improvements

* Chat history memory
* Multiple PDF support
* Streaming responses
* Source citations for answers
* Cloud deployment (AWS / HuggingFace Spaces)

---

## 📜 License

This project is open-source and free to use for learning and development.

