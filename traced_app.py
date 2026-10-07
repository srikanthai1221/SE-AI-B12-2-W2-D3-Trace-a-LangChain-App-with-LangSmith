from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "In one sentence, what is a user story?",
    "Explain the difference between a Product Owner and a Scrum Master in about 100 words.",
    "Write a detailed onboarding guide for a new Business Analyst joining an Agile banking team. "
    "Cover the first 30 days week by week, the key ceremonies they will attend, the artefacts "
    "they own, and common mistakes to avoid.",
]

for i, p in enumerate(prompts, start=1):
    response = llm.invoke(p)
    print(f"\n===== Run {i} =====")
    print(f"PROMPT: {p}")
    print(f"ANSWER:\n{response.content}")