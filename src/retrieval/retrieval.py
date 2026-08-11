from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma


def retrieve_chunks(question):
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    embeddings = model.encode(question)

    print(type(embeddings))
    print(embeddings.shape)

    vectorstore = Chroma(
        collection_name="ro_tax",
        persist_directory="tmp/vector_db"
    )

    results = vectorstore.similarity_search_by_vector(
        embeddings, k=5
    )

    return results


if __name__ == "__main__":
    question = input("Pune intrebarea: ")

    results = retrieve_chunks(question)

    for i, result in enumerate(results, 1):
        print(f"\n--- Chunk {i} ---")
        print(result)