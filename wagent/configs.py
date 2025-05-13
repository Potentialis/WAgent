import os

EVOLUTION_INSTANCE = os.getenv("EVOLUTION_INSTANCE")
EVOLUTION_INSTANCE_KEY = os.getenv("EVOLUTION_INSTANCE_KEY")
EVOLUTION_API_KEY = os.getenv("EVOLUTION_API_KEY")
EVOLUTION_URL = os.getenv("EVOLUTION_URL")

LITELLM_API_KEY = os.getenv("LITELLM_API_KEY")
LITELLM_URL = os.getenv("LITELLM_URL")

CACHE = False


class Settings:
    title = "WAgent"
    description = "AI agent for WhastApp"
    version = "0.1.0"


class LM:
    model = "litellm_proxy/llama-3.3-70b"
    api_key = LITELLM_API_KEY
    api_base = LITELLM_URL
    temperature = 0.6
    cache = CACHE
