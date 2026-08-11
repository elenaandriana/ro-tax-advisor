from langchain_chroma import Chroma

def save_embeddings(embeddings, texts, store_name = 'tmp/vector_db'):


    """
    @param embeddings List/Numpy array of embeddings
    @return None
    """
    vectorstore = Chroma(
    collection_name="ro_tax",
    persist_directory=store_name
)
    ids = [str(i) for i in range(len(texts))]

    batch_size = 5000
    start = 0

    while start < len(texts):
       end = start + batch_size

    batch_texts = texts[start:end]
    batch_embeddings = embeddings[start:end]
    batch_ids = ids[start:end]

    vectorstore._collection.add(
        ids=batch_ids,
        documents=batch_texts,
        embeddings=batch_embeddings.tolist()
    )

    start = end