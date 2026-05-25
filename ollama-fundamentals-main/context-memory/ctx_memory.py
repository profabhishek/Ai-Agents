import json
from typing import Dict, List

from openai import OpenAI
import sys

def initialiZe_client(use_ollama: bool = False) -> OpenAI:
    """Initialize the OpenAI client with the appropriate API Key for either OpenAi or Ollama"""
    if use_ollama:
        return OpenAI(base_url="http://localhost:11434/v1" ,api_key="ollama")
    
    return OpenAI()

def create_initial_messages() -> List[Dict[str, str]]:
    """ Create the initial memory for the context memory."""
    return [
        {"role":"system", "content":"You are a chess grandmaster"}
    ]

def chat(user_input: str, messages: List[Dict[str, str]], client: OpenAI, model_name: str) -> str:
    """Handle user input and generate responses"""
    
    messages.append({"role" : "user", "content":user_input})

    try:
        response = client.chat.completions.create(model=model_name, messages=messages)

        assistant_response = response.choices[0].message.content
        messages.append({"role" : "assistant", "content":assistant_response})
        return assistant_response
    
    except Exception as e:
        return(f"Error with API: {str(e)}")
    

def summarize_messages(messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Summarize older messages to save tokens"""

    old_messages = messages[:-5]
    recent_messages = messages[-5:]

    summary = "Previous conversation summarized: " + " ".join(
        [m["content"][:50] + "..." for m in old_messages]
    )
    return [
        {"role": "system", "content":summary}
    ] + recent_messages

def save_conversation(
        messages: List[Dict[str, str]], filename:str = "conversation.json" 
):
    """Save conversation to a file"""
    with open(filename, "w") as f:
        json.dump(messages, f)

def load_conversation(filename: str = "conversation.json") -> List[Dict[str, str]]:
    """ Load the conversation from a file"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No file found at {filename}")
        return create_initial_messages()
    
def main():
    print("Select model type: ")
    print("1. OpenAI GPT-4")
    print("2. Ollama (Local)")

    choice = input("Enter choice (1 or 2): ")
    use_ollama = choice == "2"

    client = initialiZe_client(use_ollama)
    model_name = "llama3.2-vision" if use_ollama else "gpt-4o-blabla"

    messages = create_initial_messages()

    print(f"\n Using {'Ollama' if use_ollama else 'OpenAI'} model. Type something to check")
    print("Available Commands: ")
    print("- 'save': Save Conversation")
    print("- 'load': Load conversation")
    print("- 'summary': Summarize conversation")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["quit", "exit"]:
            break
        elif(user_input.lower() == "save"):
            save_conversation(messages)
            print("Conversation saved!")
            continue

        elif(user_input.lower() == "load"):
            messages = load_conversation()
            print("Conversation loaded!")
            continue         

        elif(user_input.lower() == "summary"):
            messages = summarize_messages(messages)
            print("\nConversation summarized!")
            continue

        response = chat(user_input, messages, client, model_name)
        print(f"\nAssistant: {response}")

        if len(messages) > 10:
            messages = summarize_messages(messages)
            print("\n Conversation automatically summarized!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nChat session ended by user. Goodbye!")
        sys.exit()  