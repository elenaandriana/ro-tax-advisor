

from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
import re


def chunk(input_file: str):
    converter = DocumentConverter()
    result = converter.convert(input_file)
    
    text = result.document.export_to_markdown()

    chunker = HybridChunker()
    chunks_list = list(chunker.chunk(result.document))

    contextualized_chunks = build_context(chunks_list, chunker)


    print(contextualized_chunks[2008])
    print("-------------------------")
    print(contextualized_chunks[5008])

    print(f"Number of chunks: {len(chunks_list)}")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return contextualized_chunks
    
    
def build_context(chunks_list, chunker):
    contextualized_chunks = []

    for chunk in chunks_list:
        text = chunker.contextualize(chunk)

        contextualized_chunks.append({
            "text": text
        })

    return contextualized_chunks
    


chunk("Legea nr.227_2015.html")