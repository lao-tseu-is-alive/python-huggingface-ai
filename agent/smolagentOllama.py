import logging

from smolagents import CodeAgent
from OllamaModel import OllamaModel

# Basic Configuration (Simplest)
logging.basicConfig(level=logging.WARN)  # Set root logger to DEBUG

# More Control (Recommended)
logger = logging.getLogger(__name__)  # Get a logger for the current module
logger.setLevel(logging.WARNING)         # Set the logger's level


# Initialize your Ollama model (for example, using the "mistral" model)
ollama_model = OllamaModel("mistral:latest")

# Create a CodeAgent instance with the model
agent = CodeAgent(
    tools=[],              # You can add tools here (e.g., web search tools) if needed
    model=ollama_model,    # Your custom model wrapper
    planning_interval=3    # (Optional) Re-plan every 3 steps

)

# Run the agent with a prompt
logger.log(logging.DEBUG, "### Running the agent with a prompt")
result = agent.run("Who is ?")
print(result)
