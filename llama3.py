import ollama

import ollama

help(ollama.create)

modelfile = """
FROM llama3.2
SYSTEM You are very smart assistant who knows everything about oceans.
PARAMETER temperature 0.1
"""

ollama.create(
    model="knowitall",
    modelfile=modelfile
)

res = ollama.generate(
    model="knowitall",
    prompt="why is the ocean so salty?"
)

print(res["response"])

ollama.delete("knowitall")