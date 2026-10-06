import asyncio
from test_ollama import (
    init_agent,
    init_embedding,
    init_llm,
    load_documents_and_init_index,
)


async def run_chat_loop(agent):
    while True:
        user_prompt = input("Frag mich aus: ").strip()

        if user_prompt.lower() == "exit":
            return

        if not user_prompt:
            continue

        try:
            response = await agent.run(user_prompt)
            print(response)
        except Exception as exc:
            print(f"An error occurred while running the agent: {exc}")

async def async_main():
    print("Initialisiere LLM und Embedding Model...")
    init_llm()
    init_embedding()

    print("Lade Dokumente aus dem Ordner 'data'...")
    load_documents_and_init_index()

    print("Starte den Agenten...")
    agent = init_agent()

    print("Agent soweit. Was willst du über deine PDFs wissen?")

    await run_chat_loop(agent)

if __name__ == "__main__":
    asyncio.run(async_main())