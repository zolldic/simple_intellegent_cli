#!/usr/bin/python3

from .model import Client
from .storage import Storage


def main() -> None:

    client = Client()
    storage = Storage()
    storage.init_storage()

    messages = storage.load()

    while True:
        user_input: str = input("U~: ")
        messages.append({"role": "user", "content": user_input})

        if user_input == 'exit':
            break

        reply = client.send_message(user_input)
        print(f'AI~: {reply}')
        
        messages.append({"role": "assistant", "content": reply})
        storage.save(messages)
