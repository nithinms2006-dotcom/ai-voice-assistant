import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself briefly."
        }
    ]
)

print("AI:", response["message"]["content"])