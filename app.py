# Set env var OPENAI_API_KEY or load from a .env file:
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import create_extraction_chain
from langchain.callbacks import get_openai_callback
from langchain.schema import HumanMessage
from dotenv import load_dotenv

## Schema
schema_looks = {
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "integer"},
        "hair_color": {"type": "string"},
    },
    "required": ["name", "height"],
}

schema_hotel = {
    "properties": {
        "location": {"type": "string"},
        "max_price": {"type": "number"},
        "features": {"type": "string"},
    },
    "required": ["location"],
}

# Input 
inp_looks = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""
inp_hotel = """Find beachfront hotels in San Diego for less than $300 a month with free breakfast."""

# Run chain
load_dotenv()
llm = AzureChatOpenAI(
    deployment_name="openai-gpt-4-deployment",
    model= "gpt-4",
)

## shows the function
chain = create_extraction_chain(schema_hotel, llm)
print(chain.run(inp_hotel))
