import ollama

def generate_response(prompt, image_path=None):
    message = {
        "role": "user",
        "content": prompt
    }

    if image_path:
        message["images"] = [image_path]

    response = ollama.chat(
        model="llama3.2-vision",
        messages=[message]
    )

    return response["message"]["content"]


def interactive_demo():

    print("\n CLI Image and Text LLM")
    print("Type 'quit' anytime to exit")

    while True:
        prompt = input("\n Enter your prompt: ")
        if(prompt.lower() == 'quit'):
            break

        image_path = input("Enter your imgae path or (press Enter for text only): ")
        if image_path.strip() == "":
            image_path = None

        print("\nGenerating Response...")
        response = generate_response(prompt, image_path)
        print(response)    

interactive_demo()