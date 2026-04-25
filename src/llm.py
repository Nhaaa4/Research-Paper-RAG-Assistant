import os

from langchain_ollama import ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


DEFAULT_OLLAMA_MODEL = "qwen3.5"
DEFAULT_HUGGINGFACE_MODEL = "Qwen/Qwen3-8B"
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"


def get_llm(provider="ollama", model_name=None, temperature=0.1):
    if provider == "ollama":
        return ChatOllama(
            model=model_name or DEFAULT_OLLAMA_MODEL,
            temperature=temperature,
        )

    if provider == "huggingface":
        endpoint = HuggingFaceEndpoint(
            repo_id=model_name or DEFAULT_HUGGINGFACE_MODEL,
            task="text-generation",
            temperature=temperature,
            max_new_tokens=1024,
            do_sample=False,
            return_full_text=False,
        )
        return ChatHuggingFace(llm=endpoint)

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=model_name or DEFAULT_GEMINI_MODEL,
            temperature=temperature,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    raise ValueError("provider must be 'ollama', 'huggingface', or 'gemini'")
