def get_retriever(vectorstore, k: int = 4):
    retriever = QdrantVectorStore.from_existing_collection(
    embedding=emmbeddings,
    url=QDRANT_URL,
    collection_name="learning_langchain",
    
   )
    
    return retriever
    # search_result = retriever.similarity_search(
    #     query="What is the capital of France?",
        
    # )
    # return search_result
