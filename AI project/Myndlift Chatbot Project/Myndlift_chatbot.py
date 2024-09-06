from openai import OpenAI
client = OpenAI()

# Creating a thread

thread = client.beta.threads.create()
print(thread)

# Create a message

while True:
    current_input = input('You: ')
    if current_input.lower() == 'quit':
        break
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role='user',
        content=current_input
    )

    # Run the assistant

    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = 'asst_L0HdRQlVAHdA2bWNcHVuydCO'
    )

    # Display assistant response:

    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )

    # Retrieve all of the messages:

    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )
        
    for message in reversed(messages.data):
        print(message.role + ': ' + message.content[0].text.value)