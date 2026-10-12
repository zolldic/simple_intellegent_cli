#!/usr/bin/python3

from .model import Client
from .storage import Storage
import argparse
import sys

def main() -> None:

    client = Client()
    storage = Storage()
    storage.init_storage()


    parser = argparse.ArgumentParser(description="A simple ai assistant")

    # change the system prompt, 
    parser.add_argument('--system', action='store', nargs=1)
    # extract structured data, effect the response of the model.
    parser.add_argument('--structured', action='store', nargs=1)
    # clear storage. either specifiy the name, or clear all.
    parser.add_argument('--clear', action='store', nargs=1)


    args = parser.parse_args()

    if is_interactive():
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
    else:
        print(args)

def is_interactive():
    return hasattr(sys, 'ps1') or bool(sys.flags.interactive)
