import json
import pathlib

geni_block = {
    "transaction": {
        "sender": "geni_sender",
        "receiver": "geni_receiver",
        "amount": "0",
        "hashed_key": "there_is_no_key"
    }
}


def make_block(sender, receiver, hashed_key, amount):
    return


def check_if_file_is():
    file = pathlib.Path('blockchain.json')
    if not file.exists():
        print("WARNING: Removing blockchain.json")
        file.touch()
        f = open(file, "w")
        json.dump(geni_block, f)
        f.close()