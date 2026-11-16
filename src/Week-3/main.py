
import os
import traceback
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

from usage_logger import UsageLogger


def main():

    load_dotenv(override=True)

    print("=" * 40)
    print("       WEEK 3: LLM MONITORING")
    print("=" * 40)

    usage_logger = None

    try:
        # Connect to MongoDB Atlas
        usage_logger = UsageLogger()

        print("\n1. Gemini")
        print("2. Ollama")

        choice = input("\nSelect provider (1/2): ").strip()

        if choice == "1":

            api_key = os.getenv("GEMINI_API_KEY")

            if not api_key:
                raise ValueError("Gemini API key missing in .env")

            provider = GeminiProvider(api_key)

        elif choice == "2":

            provider = OllamaProvider("llama3.2")

        else:
            raise ValueError("Invalid selection. Choose 1 or 2.")

        # Create LLM client with the actual MongoDB logger
        client = LLMClient(
            provider = provider,
            usage_logger=usage_logger
        )

        prompt = input("\nEnter your question: ")

        answer = client.generate(prompt)

        print("\n========== LLM RESPONSE ==========")
        print(answer)

    except Exception as error:

        print("\nApplication error:", repr(error))
        traceback.print_exc()

    finally:

        if usage_logger is not None:
            usage_logger.close()


if __name__ == "__main__":
    main()

