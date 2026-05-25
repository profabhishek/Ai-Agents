from openai import OpenAI

import sys

def simple_chat_without_memory(user_input: str, use_ollama: bool = True) -> str:
    """
    This function demonstrate a chatbot without context/memory management.
    Each call is dependent and has no knowledge of previous interactions. 
    """

    if use_ollama:
        client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        model_name = "llama3.2-vision"
    else:
        client = OpenAI()
        model_name = "gpt-4o-mini"

    try:
        response = client.chat.completions.create(
            model=model_name, messages=[{"role":"user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
    
def main():

    print("\n===Simple chatbot without memory")
    print("Notice how chatbot dont remember anything from the previous messages!")
    print("/n Select any model type")
    print("1. OpenAI GPT-4")
    print("2. Ollama 3.2 vision")

    while True:
        choice = input("\n Enter your choice (1 or 2): ").strip()
        if choice in ["1", "2"]:
            break
        print("Please Enter either 1 or 2")

    use_ollama = choice == "2"

    print("\n === Chat Session Started ===")
    print("\n Type 'quit' or 'exit' to save the conversation")
    print("Type 'clear' to clear the screen")
    print("Each message is inpendent - the bot has no memory of previous messages!")

    while True:
        user_input = input("\n You: ").strip()

        if user_input.lower() in ["quit", "exit"]:
            print("\n GoodBye!")
            sys.exit()

        if user_input.lower() == "clear":
            print("\033[H\033[J", end="")
            continue 
        
        if not user_input:
            continue

        response = simple_chat_without_memory(user_input, use_ollama)
        print(f"\nBot: {response}")

        print("\n" + "-" * 50)

if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print("\n\nChat session ended by user. GoodBye")
        sys.exit()