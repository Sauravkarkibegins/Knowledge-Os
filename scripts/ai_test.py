import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Explain git branches simply'}
    ]
)

print(response['message']['content'])