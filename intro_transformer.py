from transformers import pipeline

def create_simple_llm():
    generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    return generator

generator = create_simple_llm()
prompt = "He was such a man in the "
generated_text = generator(prompt, max_length=100, num_return_sequences=1)
print(generated_text[0]["generated_text"])