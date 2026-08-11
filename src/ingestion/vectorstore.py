from langchain_chroma import Chroma

def save_embeddings(embeddings, texts, store_name='tmp/vector_db'):
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
    print("Saving embeddings to vectorstore...")

    while start < len(texts):
        print("Start batch:", start)
        end = start + batch_size

        batch_texts = texts[start:end]
        batch_ids = ids[start:end]
        batch_embeddings = embeddings[start:end]

        if hasattr(batch_embeddings, "tolist"):
            batch_embeddings = batch_embeddings.tolist()
        else:
            batch_embeddings = list(batch_embeddings)

        print("Batch ready:", len(batch_texts))

        vectorstore._collection.add(
            documents=batch_texts,
            ids=batch_ids,
            embeddings=batch_embeddings
        )
        print("Batch saved.")

        start = end  

    print("All embeddings saved successfully.")