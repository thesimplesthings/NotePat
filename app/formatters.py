import logging
from abc import ABC, abstractmethod

import openai

from app.settings import CHATGPT_KEY, DEFAULT_SYSTEM_PROMP

logger = logging.getLogger(__name__)


class TextFormatterError(Exception):
    pass


class TextFormatter(ABC):
    @abstractmethod
    def format_text(self, text: str) -> str | None:
        pass


class ChatGPTFormatter(TextFormatter):
    def __init__(self, api_key: str = CHATGPT_KEY):
        self.system_prompt = self._get_system_prompt()
        self._set_api_key(api_key)

    def _get_system_prompt(self) -> str:
        try:
            with open("app/assets/prompts/custom_prompt.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            logger.warning("Custom system prompt file not found, using default system prompt.")
            return DEFAULT_SYSTEM_PROMP

    def _set_api_key(self, api_key: str) -> None:
        if not api_key:
            raise EnvironmentError("API key not found in environment variables.")

        openai.api_key = api_key

    def format_text(self, text: str) -> str | None:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": self.system_prompt}, {"role": "user", "content": text}],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise TextFormatterError(f"An error occurred with ChatGPT: {e}")


def get_formatter() -> TextFormatter:
    return ChatGPTFormatter()
