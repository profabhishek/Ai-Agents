import ollama

response = ollama.list()
# print(response)

res = ollama.chat(
    model="llama3.2-vision",
    messages = [
        {
            "role": "user",
            "content": "My name is Abhishek"
        },
        {
            "role": "assistant",
            "content": "Nice to meet you Abhishek"
        },
        {
            "role": "user",
            "content": "What is my name?"
        }
    ],
    stream=True
)

# for chunk in res:
#     print(chunk["message"]["content"], end="", flush=True)


res = ollama.generate(
    model= "llama3.2-vision",
    prompt= "Once upon a time"
)
# print(res1["response"])


ollama.create(
    model="chessmaster",
    from_="llama3.2-vision",
    system="You are a chess expert who explains chess clearly and informatively.",
    parameters={
        "temperature": 1.0
    }
)

res = ollama.generate(
    model="chessmaster",
    prompt="What is the best opening move in chess?"
)
# print(res["response"])

ollama.delete("knowitall")