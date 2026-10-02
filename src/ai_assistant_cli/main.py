

from .model import Client

def main() -> None:

    client = Client()

    while True:
        user_input = input("U~: ")

        if user_input == 'quit':
            break

        reply = client.send_message(user_input)

        print(f'AI~: {reply}')
