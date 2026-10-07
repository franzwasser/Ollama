import asyncio
from test_ollama import (
    init_agent,
    init_embedding,
    init_llm,
    load_documents_and_init_index,
)


async def run_chat_loop(agent):
    while True:
        user_prompt = input("Your prompt ").strip()

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
    print("Initializing LLM and Embedding model...")
    init_llm()
    init_embedding()

    print("loading docs from dir 'data'...")
    load_documents_and_init_index()

    print("starting agent...")
    agent = init_agent()

    print("agent ready. Type 'exit' to quit.")

    await run_chat_loop(agent)

if __name__ == "__main__":
    asyncio.run(async_main())