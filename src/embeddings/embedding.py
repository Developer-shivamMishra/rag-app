from langchain_google_genai import GoogleGenerativeAIEmbeddings



def get_embeddings():
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        api_key=os.getenv("GEMINI_API_KEY")
    )
    
    return embeddings








