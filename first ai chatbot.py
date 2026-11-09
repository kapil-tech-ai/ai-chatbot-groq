from groq import Groq
api_key = "Paste your API Key Here"
client = Groq(api_key=api_key)
print("AI Chatbot is running. Type 'exit' to quit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        print("Chatbot is stopping. Goodbye!")
        break
    chat_completions = client.chat.completions.create(
        messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                   {"role": "user", "content": user_input}],
        model="openai/gpt-oss-120b"
    )
    print("AI:", chat_completions.choices[0].message.content)