# Research Paper RAG Assistant

<p align="center">
  <img src="assets/architecture.png" alt="Architecture Diagram" width="900"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red" />
  <img src="https://img.shields.io/badge/RAG-LangChain-green" />
  <img src="https://img.shields.io/badge/Search-Elasticsearch-yellow" />
  <img src="https://img.shields.io/badge/LLM-Ollama%20%7C%20HuggingFace%20%7C%20Gemini-purple" />
  <img src="https://img.shields.io/badge/License-MIT-black" />
</p>

## Overview

Research Paper RAG Assistant is an AI chatbot for asking questions over multiple research paper PDFs. Users can upload one or more papers, process them into searchable chunks, and ask natural language questions through a Streamlit interface.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant context before generating an answer. It supports both one-column and two-column PDF layouts, preserves source metadata, and uses hybrid search to combine semantic vector retrieval with keyword-based BM25 retrieval.

## Features

- Multi-PDF upload
- Layout-aware PDF parsing for one-column and two-column documents
- Text chunking with metadata preservation
- Embedding generation for semantic search
- Elasticsearch hybrid search using vector similarity and BM25 keyword retrieval
- LLM support through Ollama and Google Gemini
- Source citations with filename and page number
- Streamlit web interface

## Architecture

The application follows a standard RAG pipeline:

```text
PDF Upload
   |
Layout-Aware PDF Extraction
   |
Text Chunking
   |
Embedding Generation
   |
Elasticsearch Indexing
   |
Hybrid Retrieval
   |
LLM Answer Generation
   |
Answer with Source Citations
```

## Tech Stack

- Python
- Streamlit
- LangChain
- Elasticsearch
- Hugging Face embeddings
- Ollama
- Google Gemini

## Project Structure

```text
.
├── app.py
├── README.md
├── requirements.txt
├── html_template.py
├── data/
└── src/
    ├── chunk_splitter.py
    ├── embeddings.py
    ├── llm.py
    ├── pdf_loader.py
    ├── rag.py
    └── vector_db.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nhaaa4/Research-Paper-RAG-Assistant.git
cd Research-Paper-RAG-Assistant
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

```bash
# On Windows:
.venv\Scripts\activate
# On macOS or Linux:
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file for HuggingFace and Gemini support:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
GOOGLE_API_KEY=your_google_api_key_here
```

## Run Elasticsearch

Start Elasticsearch with Docker:

```bash
docker compose up
```

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Configuration

Embedding options:

```text
huggingface
ollama
```

LLM options:

```text
huggingface
ollama
gemini
```

Common configuration values:

```python
chunk_size = 1000
chunk_overlap = 200
top_k = 5
temperature = 0.1
```

These values can be adjusted in the relevant source files or through the Streamlit UI where available.

## Usage

1. Start Elasticsearch.
2. Start the Streamlit application.
3. Upload one or more research paper PDFs.
4. Select the embedding provider.
5. Select the LLM provider.
6. Click `Process PDFs`.
7. Ask questions about the uploaded papers.
8. Review the answer and cited sources.

## Example Questions

```text
Summarize the main contribution of this paper.
```

```text
What method does the paper propose?
```

```text
Which datasets are used in the experiments?
```

```text
How does this method compare with previous approaches?
```

```text
What are the main limitations mentioned by the authors?
```

## Limitations

- Answer quality depends on PDF text extraction quality.
- The system only answers from uploaded documents and does not use external knowledge.
- Large PDFs or many uploaded files can increase processing time.
- Scanned PDFs may require OCR before they can be processed accurately.
- Complex tables, equations, and figures may not be fully captured as text.

## Future Improvements

- Add a reranker for improved retrieval precision.
- Highlight cited source passages in the UI.
- Add evaluation metrics for retrieval and answer quality.
- Support multilingual research papers.
- Add OCR support for scanned PDFs.
- Add document-level filtering and advanced metadata search.

## Demo

<p align="center">
  <img src="assets/demo_1.png" alt="Demo 1" width="900"/>
  <img src="assets/demo_2.png" alt="Demo 2" width="900"/>
</p>

## License

MIT License
