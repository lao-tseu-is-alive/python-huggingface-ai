import logging
from dataclasses import dataclass
import ollama

# Basic Configuration (Simplest)
logging.basicConfig(level=logging.DEBUG)  # Set root logger to DEBUG

# More Control (Recommended)
logger = logging.getLogger(__name__)  # Get a logger for the current module
logger.setLevel(logging.DEBUG)         # Set the logger's level


@dataclass
class Message:
    content: str

class OllamaModel:
    def __init__(self, model_name: str):
        self.model_name = model_name
        logger.info(f"OllamaModel initialized with model_name: {model_name}")
        self.client = ollama.Client()  # assumes ollama.Client() initializes the client

    def __call__(self, messages, **kwargs):
        # Format messages for Ollama's API
        logger.info(f"Ollama input messages: {repr(messages)}")
        formatted_messages = []
        for msg in messages:
            if isinstance(msg, str):
                logger.info(f"Ollama input message is str: {msg}")
                formatted_messages.append({"role": "user", "content": msg})
            elif isinstance(msg, dict):
                logger.info(f"Ollama input message is dict: {repr(msg)}")
                role = msg.get("role", "user")
                # If role is an enum, get its value (or cast to string)
                role_str = str(role) if not isinstance(role, str) else role
                content = msg.get("content", "")
                # If the content is a list, join it into one string.
                if isinstance(content, list):
                    content = " ".join(item.get("text", "") for item in content if isinstance(item, dict))
                formatted_messages.append({"role": role_str, "content": content})
                logger.info(f"Ollama formatted message: {repr(formatted_messages[-1])}")
            else:
                logger.info(f"Ollama input message is neither str nor dict: {msg}")
                formatted_messages.append({"role": "user", "content": str(msg)})

        # Call the Ollama chat API
        response = self.client.chat(
            model=self.model_name,
            messages=formatted_messages,
            options={'temperature': 0.7, 'stream': False}
        )
        # Return a Message with the generated content
        logger.info(f"Ollama response: {repr(response)}")
        # Extract the raw content from the response
        raw_content = response.get("message", {}).get("content", "")
        # If raw_content is a list, join the text from each dictionary into a single string
        if isinstance(raw_content, list):
            final_content = " ".join(
                item.get("text", "") for item in raw_content if isinstance(item, dict)
            )
        else:
            final_content = raw_content
        # Return a Message with the validated string content
        print(f"#### Ollama final content: {repr(final_content)}")
        return Message(content=final_content)
