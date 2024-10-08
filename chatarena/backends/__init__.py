from ..config import BackendConfig

from .base import IntelligenceBackend
from .openai import OpenAIChat
from .cohere import CohereAIChat
from .llama2 import LLamaChat
from .human import Human
from .hf_transformers import TransformersConversational
from .anthropic import Claude

ALL_BACKENDS = [
    Human,
    OpenAIChat,
    CohereAIChat,
    TransformersConversational,
    Claude,
    LLamaChat
]

BACKEND_REGISTRY = {backend.type_name: backend for backend in ALL_BACKENDS}


# Load a backend from a config dictionary
def load_backend(config: BackendConfig):
    try:
        backend_cls = BACKEND_REGISTRY[config.backend_type]
    except KeyError:
        raise ValueError(f"Unknown backend type: {config.backend_type}")

    backend = backend_cls.from_config(config)
    return backend
