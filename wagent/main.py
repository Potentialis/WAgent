from fastapi import FastAPI
from routers import webhook_router
import dspy
import mlflow
import os


LITELLM_API_KEY = os.environ["LITELLM_API_KEY"]
LITELLM_URL = os.environ["LITELLM_URL"]

mlflow.set_tracking_uri("https://mlflow.su3h7am.site")
mlflow.set_experiment("dspy_chatbot")
mlflow.autolog(exclude_flavors=["litellm", "openai"])

lm = dspy.LM(
    model="litellm_proxy/llama-3.3-70b",
    api_key=LITELLM_API_KEY,
    api_base=LITELLM_URL,
    temperature=0.6,
    cache=False,
)

dspy.configure(lm=lm)

app = FastAPI(
    title="DSPy Program API",
    description="A simple API serving a DSPy Chain of Thought program",
    version="1.0.0",
)

app.include_router(webhook_router)
