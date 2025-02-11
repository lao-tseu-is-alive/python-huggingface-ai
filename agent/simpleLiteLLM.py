from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama/deepseek-r1:latest",
    api_base="http://localhost:11434",
    num_ctx=8192 # ollama default is 2048 which will fail horribly. 8192 works for easy tasks, more is better. Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to calculate how much VRAM this will need for the selected model.
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True, max_steps=12)

question_asked="Could you give me the 118th number in the Fibonacci sequence?"
print("Running agent...")

agent.run(question_asked)
print("Question asked: ", question_asked)
correct_answer="2046711111473984623691759"
correct_answer_formated="2,046,711,111,473,984,623,691,759"
print(f"Answer should be : {correct_answer}")
print(f"Answer formated  : {correct_answer_formated}")
