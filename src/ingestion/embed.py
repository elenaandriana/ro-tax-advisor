from sentence_transformers import SentenceTransformer
from typing import List

def embed(chunks: List):
    """
    @param chunks Chunks of text
    @return List / Numpy array of embeddings 
    """
    model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

    embeddings = model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)

    return embeddings