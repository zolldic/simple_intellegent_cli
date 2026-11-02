#!/usr/bin/python3

from .model import Client
from .storage import Storage
import argparse
import sys

from typing import List

def main() -> None:

    client = Client()
    storage = Storage()
    path = storage.init_storage()

    parser = argparse.ArgumentParser(description="A simple ai assistant")

    command = parser.add_argument("prompt", nargs="?", type=str, help="prompt to the LLM")
    # change the system prompt, 
    parser.add_argument('--system', action='store', nargs=1)
    # extract structured data, effect the response of the model.
    parser.add_argument('--structured', action='store', type=str, nargs=1)
    # clear storage. either specifiy the name, or clear all.
    parser.add_argument('--clear', action='store', nargs=1)


    args = parser.parse_args()

    if args.system:
        data = storage.load()
        for d in data:
            if d["role"] == "system":
                d["content"] = args.system[0]
        storage.save(data)

        return

    if args.structured:
        context = [
            {"role": "system", "content": "Extract invoice details from the text."},
            {"role": "user", "content": args.structured[0]}
        ]
        response = client.structured_output(context)
        print(response)
        return 

    if args.clear:
        print("clear invoke")
        return



    if not args.prompt:
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
            return
    else:
        reply = client.send_message(args.prompt)
        print(reply)
        return
