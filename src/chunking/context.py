from docling.chunking import HybridChunker


def build_context(chunks_list, chunker):
    contextualized_chunks = []
    for chunk in chunks_list:
        context = chunker.contextualize(chunk)
        contextualized_chunks.append((chunk, context))
    return contextualized_chunks 