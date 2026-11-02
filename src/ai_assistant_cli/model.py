from openai import OpenAI
from dotenv import load_dotenv
import os
from .types import Invoice

load_dotenv()


class Client:
    def __init__(self, model = "openai/gpt-oss-20b"):
        self._model = model
        self._client = OpenAI(
            api_key = os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )


    def send_message(self, prompt: str) -> str:
        response = self._client.responses.create(
            model=self._model,
            input=prompt
        )

        return response.output_text

    def structured_output(self, prompt):
        response = self._client.responses.parse(
            model=self._model,
            input=prompt,
            text_format=Invoice
        )

        return response.output_parsed

