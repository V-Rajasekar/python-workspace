import openai
import os

""" 
The code sets up a chat interaction between the user and the assistant using the OpenAI GPT-3.5-turbo model.
The base_messages list contains system and user messages that set the context for the conversation.
Inside the loop, the assistant generates a response based on the combined messages (base messages + previous responses).
The assistant’s response is printed, and the user can input the next message.
The loop continues until manually stopped. """

openai.api_key = os.environ.get("OPENAI_API_KEY", "")

base_messages = [
    {"role": "system", "content": "You are a helpful assistant built to provide guidance on doing chores."},
    {"role": "system", "content": "You're trained on blue collar jobs like manufacturing, data entry, and janitorial services."},
    {"role": "user", "content": "I need to make an appointment with Bob sagat tomorrow at 3pm"}
]

responses = []
# Start an infinite loop for the chat interaction
while True:
    # Create a chat completion using the GPT-3.5-turbo model
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=base_messages + responses
    )
    # Print the assistant's response
    print()
    print()
    print(chat_completion.choices[0].message.content)
    print()
    print()
    # Append the assistant's response to the list of responses
    responses.append({
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
        })
     # Get the user's next message
    next_message = input("Send another message: ")
     # Append the user's message to the list of responses
    responses.append({
        "role": "user",
        "content": next_message
    })
