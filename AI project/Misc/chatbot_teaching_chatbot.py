from openai import OpenAI
client = OpenAI()

# Read the document content
try:
    with open(r'C:\Users\thoma\OneDrive\Ambiente de Trabalho\AI project\gpt manual\text_generation.txt', 'r', encoding='latin-1') as file:
        document_content = file.read()
except Exception as e:
    print(f"Error reading file: {e}")
    document_content = ""


while True:
    user_input = input("You: ")
    
    if user_input == "exit":
        break

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"I want you to help and teach me how to build a chatbot using gpt API. Here is a document for you to refer to: {document_content}"},
            {"role": "user", "content": user_input}
        ]
    )

    print(completion.choices[0].message.content)