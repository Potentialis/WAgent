from fastapi import APIRouter
from models import EvoWebhookPayload
import mlflow
from services.attendant import attendant

print("routers")

webhook_router = APIRouter()


@webhook_router.post("/webhook")
async def wa(payload: EvoWebhookPayload):
    if payload.data.messageType == "conversation":
        with mlflow.start_run(run_name=payload.sender):
            attendant(payload.data.message.conversation)
