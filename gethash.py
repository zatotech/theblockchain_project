from hashlib import sha256


def newhash(y, x):
    thehash = "3333"
    while (thehash[-3] != "a") | (thehash[-2] != "b") | (thehash[-1] != "c"):
        y = y + 1
        thehash = sha256(f'{x*y}'.encode()).hexdigest()
    return thehash, y, x