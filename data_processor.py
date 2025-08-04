import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import os

# Define the directory for your knowledge base
KB_DIR = "./kb"
DOCS_DIR = "./Docs"
COLLECTION_NAME = "b2scala_knowledge"
EMBEDDING_MODEL = "nomic-embed-text" # You can choose a different embedding model from Ollama

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text
def extract_text_from_txt(txt_path):
    text = ""
    with open(txt_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def process_documents():
    """
    Loads documents, chunks them, and stores embeddings in ChromaDB.
    """
    # 1. Extract text from all PDFs in the Docs directory
    full_text = ""
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(DOCS_DIR, filename)
            print(f"Extracting text from {filename}...")
            full_text += extract_text_from_pdf(pdf_path)
        elif filename.endswith(".txt"):
            txt_path = os.path.join(DOCS_DIR, filename)
            print(f"Extracting text from {filename}...")
            full_text += extract_text_from_txt(txt_path)
    # 2. Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ";", ".", " "]
    )
    chunks = text_splitter.split_text(full_text)
    print(f"Created {len(chunks)} chunks.")

    # 3. Create embeddings and store in ChromaDB
    print(f"Initializing embedding model from Ollama ({EMBEDDING_MODEL})...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    
    print("Creating ChromaDB vector store...")
    db = Chroma.from_texts(
        chunks,
        embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=KB_DIR
    )
    db.persist()
    print("Knowledge base created successfully!")

if __name__ == "__main__":
    if not os.path.exists(DOCS_DIR):
        print(f"Error: Directory '{DOCS_DIR}' not found. Please place your PDFs here.")
    else:
        process_documents()