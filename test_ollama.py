from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.agent import AgentWorkflow
from llama_index.llms.ollama import Ollama
import os
import dotenv
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import PDFReader
import logging


#disable distracting logs
logging.basicConfig(level=logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("llama_index").setLevel(logging.WARNING)

dotenv.load_dotenv()

# fetch hf token from dotenv
HF_TOKEN = os.getenv("HF_TOKEN")

# embedding model
def init_embedding():
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-m3",
    )

# LLM model
def init_llm():
    Settings.llm = Ollama(
        model="gemma4:e2b",
        base_url="http://localhost:11434",
        request_timeout=360.0,
        context_window=8000,
    )

def load_documents_and_init_index():
    global query_engine
    reader = PDFReader()
    documents = SimpleDirectoryReader(
        "data",
        file_extractor={".pdf": PDFReader()},
        recursive=True,
    ).load_data()
    #documents = reader.load_data(file=Path("data"))
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=64)
    index = VectorStoreIndex.from_documents(
        documents,
        transformations=[splitter],
        embed_model=Settings.embed_model,
    )
    query_engine = index.as_query_engine(similarity_top_k=6)

# search documents tool
async def search_document(query: str) -> str:
    if query_engine is None:
        raise RuntimeError("Document index is not initialized. Call load_documents_and_init_index() first.")

    response = await query_engine.aquery(query)
    return str(response)


# Initialize agent
def init_agent():
    agent = AgentWorkflow.from_tools_or_functions(
        [search_document],
        llm=Settings.llm,
        system_prompt=(
        "You are a helpful assistant that answers questions using the documents loaded into the document search tool. "
        "For every question about the documents, you must call the search_document tool first. "
        "Do not say you cannot access the documents. The documents are available through the search_document tool. "
        "Base your final answer only on the information returned by the tool. "
        "If the tool does not return enough information, say that the answer was not found in the documents."
        ),
    )
    return agent
