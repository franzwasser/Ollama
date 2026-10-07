# Local PDF RAG Agent with LlamaIndex & Ollama

A local, document-based RAG agent that answers questions about your PDF files stored in the `data/` directory. 
This project integrates **LlamaIndex**, a local **Ollama LLM**, and **HuggingFace Embeddings** for privacy-focused, local document analysis.

---

##  Features

* **Local LLM Execution:** Powered by Ollama (`gemma4:e2b`) running locally without external API costs for generation.
* **High-Performance Embeddings:** Semantic vector search using the `BAAI/bge-m3` embedding model via HuggingFace with support for different languages.
* **Advanced Chunking & PDF Parsing:** Optimized text chunking with LlamaIndex's `SentenceSplitter` (chunk size: 512, overlap: 64) and a dedicated `PDFReader`.
* **Agentic Workflow:** Built using LlamaIndex's `AgentWorkflow`, enabling the agent to autonomously decide when to call the document search tool.
* **Interactive CLI:** A user-friendly command-line chat loop.

---

## ️ Prerequisites

1. **Python 3.10+**
2. **Ollama:** Installed and running on your local machine (`http://localhost:11434`).
   * Pull the target model:
     ```bash
     ollama pull gemma4:e2b
     ```

---

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/franzwasser/Ollama.git
   cd Ollama
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   HF_TOKEN=your_huggingface_token_here
   ```

5. **Add your documents:**
   Create a `data` folder in the project root and place your PDF files inside:
   ```bash
   mkdir data
   ```

---

## Usage

Start the interactive terminal chat:

```bash
python main.py
pthon3 main.py # for Mac/Linux
```

Once initialized, ask questions regarding any PDFs placed in the `data/` folder.

```text
Initializing LLM and Embedding model...
loading docs from dir 'data'...
starting agent...
agent ready. Type 'exit' to quit.

Frag mich aus: What are the main findings in the report?
...
Your prompt:
```

* **Exit:** Type `exit` to close the session.