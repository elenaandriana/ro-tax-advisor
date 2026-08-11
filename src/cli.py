

from ingestion.embed import embed
from ingestion.parse import chunk
from ingestion.vectorstore import save_embeddings

if __name__ == '__main__':
    INPUT_FILE = 'Legea nr.227_2015.html'

    chunks = chunk(INPUT_FILE)
    print("Chunks generated successfully.", len(chunks))

    texts = [chunk["text"] for chunk in chunks]
    print("Texts extracted successfully.", len(texts))

    embeddings = embed(texts)
    print("Embeddings generated successfully.")

    save_embeddings(embeddings, texts, 'tmp/vector_db')
    