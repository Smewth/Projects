from openai import OpenAI
client = OpenAI()

while True:
    user_input = input("You: ")
    
    if user_input == "exit":
        break

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I want to talk about Myndlift, it's product, and in general, Neurofeedback therapy."},
            {"role": "user", "content": user_input}
        ]
    )

    print(completion.choices[0].message.content)