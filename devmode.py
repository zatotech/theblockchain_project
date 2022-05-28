import os
import pathlib


def remove_files():
    hashfile = pathlib.Path('hashlist.txt')
    blockfile = pathlib.Path('blockchain.json')
    print("WARNING: Removing hashlist.txt")
    if hashfile.exists():
        os.remove(hashfile)

    print("WARNING: Removing blockchain.json")
    if blockfile.exists():
        os.remove("blockchain.json")