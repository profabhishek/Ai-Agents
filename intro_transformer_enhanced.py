from transformers import pipeline, AutoTokenizer

def create_simple_llm():
    generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    return generator

def generate_text(generator, prompt, max_new_tokens=100):
    result = generator(
        prompt,
        max_new_tokens = max_new_tokens,
        num_return_sequences = 1,
        do_sample = True,
        temperature = 0.7
    )
    return result[0]['generated_text']

def run_llm_demo():
    print("Loading simple LLM Model...")
    generator = create_simple_llm()

    print("\n Simple LLM Demo")
    print("This demo shows how to use a simple LLM model to generate text based on a prompt")

    prompts = [
        "Virat Kohli is a",
        "You are such a",
        "App yaha aa"
    ]

    for prompt in prompts:
        print(f"\n Prompt: {prompt}")
        generated = generate_text(generator, prompt)
        print("Generated: ")
        print(generated)
        input("\n Please press Enter to see next example...")

def interactive_demo():
    generator = create_simple_llm()

    print("\n Interactive LLM Demo")
    print("Type your own prompts (or type 'quit' to exit)")

    while True:
        prompt = input("\nEnter your prompt")
        if(prompt.lower()) == 'quit':
            break
        response = generate_text(generator, prompt)
        print("\nGenerating Response...")
        print(response)

def explain_process():

    print("\n🧠 How TinyLlama Works:")
    print("1. Input Text → Tokenization → Numbers")
    print("2. Numbers → Transformer Processing → Prediction")
    print("3. Prediction → New Tokens → Output Text")

    tokenizer = AutoTokenizer.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    )

    text = "Hello World!"
    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)

    print("\n📝 Example Tokenization:")
    print(f"Original Text: '{text}'")
    print(f"As tokens (numbers): {tokens}")
    print(f"Decoded back: '{decoded}'")


if __name__ == "__main__":
    print("Choose a demo:")
    print("1. Run basic demonstration")
    print("2. Interactive mode")
    print("3. Explain the process")

    choice = input("\n Enter your Choice (1-3): ")

    if(choice == '1'):
        run_llm_demo()

    elif (choice == '2'):
        interactive_demo()

    elif (choice == '3'):
        explain_process()

    else:
        print("Invalid Choice")        