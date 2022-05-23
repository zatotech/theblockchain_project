import os

def remove_files():
    print("WARNING: Removing haslist.txt")
    os.remove("hashlist.txt")
    print("WARNING: Removing blockchain.json")
    os.remove("blockchain.json")