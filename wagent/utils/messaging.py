from evolutionapi.client import EvolutionClient
from evolutionapi.models.message import TextMessage
import os

EVOLUTION_INSTANCE = os.environ["EVOLUTION_INSTANCE"]
EVOLUTION_INSTANCE_KEY = os.environ["EVOLUTION_INSTANCE_KEY"]
EVOLUTION_API_KEY = os.environ["EVOLUTION_API_KEY"]
EVOLUTION_URL = os.environ["EVOLUTION_URL"]

evo = EvolutionClient(base_url=EVOLUTION_URL, api_token=EVOLUTION_API_KEY)


def sendMsg(text):
    msg = TextMessage(number="5562994282491", text=text, delay=1000)

    evo.messages.send_text(
        instance_id=EVOLUTION_INSTANCE,
        instance_token=EVOLUTION_INSTANCE_KEY,
        message=msg,
    )
