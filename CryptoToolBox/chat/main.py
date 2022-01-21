import CryptoToolBox.chat.client as client
import CryptoToolBox.chat.server as server
from CryptoToolBox.helpers.generic_cli import generic_cli

menu = {
    "a": {"message": "Run client", "func": client.run_client},
    "b": {"message": "Run server", "func": server.run_server},
}


def chat_room_cli():
    generic_cli(menu=menu)
