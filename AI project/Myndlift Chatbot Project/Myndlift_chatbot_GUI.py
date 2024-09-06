import customtkinter as ctk
from openai import OpenAI
client = OpenAI()

# Creating a thread
thread = client.beta.threads.create()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def send_message():
    user_message = user_input.get()
    user_input.delete(0)

    # Create a message
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role='user',
        content=user_message
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = 'asst_L0HdRQlVAHdA2bWNcHVuydCO'
    )

    # Wait for the run to complete
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )
        if run.status == 'completed':
            break

    # Retrieve all of the messages
    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    for message in reversed(messages.data):
        chat_history.insert('end', message.role + ': ' + message.content[0].text.value + '\n')

root = ctk.CTk()

chat_history = ctk.CTkTextbox(root, width=1500, height=500)
chat_history.pack()

user_input = ctk.CTkEntry(root, width=500)
user_input.pack()

user_input.bind("<Return>", lambda event: send_message())

send_button = ctk.CTkButton(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()