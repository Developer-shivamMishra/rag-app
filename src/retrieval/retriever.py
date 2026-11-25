def get_retriever(vectorstore, k: int = 4):
    return vectorstore.as_retriever(search_kwargs={"k": k})