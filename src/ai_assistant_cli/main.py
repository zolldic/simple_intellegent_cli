#!/usr/bin/python3

from .model import Client
from .storage import Storage
import argparse
import sys

def main() -> None:

    client = Client()
    storage = Storage()
    storage.init_storage()

    messages = storage.load()

    parser = argparse.ArgumentParser(description="A simple ai assistant")
    
    # change the system prompt, 
    parser.add_argument('--system', action='store', nargs=1)
    # extract structured data, effect the response of the model.
    parser.add_argument('--structured', action='store', nargs=1)
    # clear storage. either specifiy the name, or clear all.
    parser.add_argument('--clear', action='store', nargs=1)

        if user_input == 'exit':
            break

        reply = client.send_message(user_input)
        print(f'AI~: {reply}')
        
        messages.append({"role": "assistant", "content": reply})
        storage.save(messages)
