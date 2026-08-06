from unittest import result

from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker

def chunk(input_file: str):
    converter = DocumentConverter()
    result = converter.convert(input_file)
    
    text = result.document.export_to_markdown()

    chunker = HybridChunker()
    chunks_list = list(chunker.chunk(result.document))

    
    print(f"Number of chunks: {len(chunks_list)}")
    f = open("output.txt", "w", encoding="utf-8")
    f.write(text)
    f.close()
   
    
    """""
    @param input_file HTML input file
    @return Tuple of chunks and their metadata
    """


chunk("Legea nr.227_2015.html")