from openai import OpenAI
client = OpenAI()

# Uploading file to Open AI

file = client.files.create(
    file=open(r'C:\Users\thoma\OneDrive\Ambiente de Trabalho\AI project\gpt manual\text_generation.txt', 'rb'),
    purpose = "assistants"
)
print(file)

#Creating the assistant

assistant = client.beta.assistants.create(
    name = "Myndlift bot",
    instructions = "You are going to use the documents I provide to give me the most accurate answers about anything related to Myndlift. The documents I provide will always be a priority",
    tools = [{"type": "retrieval"}],
    model = "gpt-3.5-turbo-1106",
    file_ids = ["file-alxR96yDgmS4P6N1aqUCxz8N"]
)

print(assistant.id)
