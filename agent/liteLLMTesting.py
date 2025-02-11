

from litellm import completion

question_text = "What is the capital of France?"
messages = [{"role": "user", "content": question_text}]

response = completion(
    model="ollama/mistral:latest",
    messages=messages,
    api_base="http://localhost:11434"
)
print(response)
print(response.choices[0].get("message", {}).get("content", "No response found"))