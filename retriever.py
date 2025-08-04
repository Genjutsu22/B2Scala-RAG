from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Define the directory for your knowledge base
KB_DIR = "./kb"
COLLECTION_NAME = "b2scala_knowledge"
EMBEDDING_MODEL = "nomic-embed-text"

def retrieve_context(query, k=5):
    """
    Retrieves the most relevant chunks from the ChromaDB knowledge base.
    
    Args:
        query (str): The structured protocol draft to use as a query.
        k (int): The number of top-k documents to retrieve.

    Returns:
        list: A list of relevant document chunks.
    """
    print("Loading ChromaDB knowledge base...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    db = Chroma(
        persist_directory=KB_DIR,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )
    
    print(f"Retrieving top {k} relevant documents for the query...")
    retrieved_docs = db.similarity_search(query, k=k)
    
    return [doc.page_content for doc in retrieved_docs]

if __name__ == "__main__":
    # This is an example of how the retriever can be used
    example_query = "Define an agent named Alice that uses the primitives tell and get."
    context = retrieve_context(example_query)
    print("\n--- Retrieved Context ---")
    for doc in context:
        print(doc)
        print("---")