from transformers import AutoTokenizer, pipeline


def create_simple_llm():

    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    generator = pipeline("text-generation",model=model_name)

    return generator


def generate_text(generator, prompt, max_new_tokens=100):

    result = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    return result[0]['generated_text']


def run_llm_demo():

    print("Loading simple LLM model...")
    generator = create_simple_llm()

    print("\nSimple LLM Demo")
    print("This demo shows how to use a simple LLM model to generate text based on a prompt.")

    prompts = [
        "The quick brown fox",
        "Once upon a time",
        "Python programming is"
    ]

    for prompt in prompts:

        print(f"\nPrompt: {prompt}")

        generated = generate_text(generator, prompt)

        print("Generated:")
        print(generated)

        input("\nPress Enter to see the next example...")


def interactive_demo():

    generator = create_simple_llm()

    print("\nInteractive LLM Demo")
    print("Type your own prompts (or type 'exit' to quit)")

    while True:

        prompt = input("\nEnter a prompt: ")

        if prompt.lower() == 'exit':
            break

        response = generate_text(generator, prompt)

        print("\nGenerated response:")
        print(response)


def explain_process():

    print("\n🧠 How TinyLlama Works:")
    print("1. Input Text → Tokenization → Numbers")
    print("2. Numbers → Transformer Processing → Prediction")
    print("3. Prediction → New Tokens → Output Text")

    tokenizer = AutoTokenizer.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    )

    text = "Hello world!"

    tokens = tokenizer.encode(text)

    decoded = tokenizer.decode(tokens)

    print("\n📝 Example Tokenization:")
    print(f"Original text: '{text}'")
    print(f"As tokens (numbers): {tokens}")
    print(f"Decoded back: '{decoded}'")


if __name__ == "__main__":

    print("Choose a demo:")
    print("1. Run basic demonstration")
    print("2. Interactive mode")
    print("3. Explain the process")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':

        run_llm_demo()

    elif choice == '2':

        interactive_demo()

    elif choice == '3':

        explain_process()

    else:

        print("Invalid choice!")