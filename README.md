<h1>Python Blockchain and Hashing project</h1>
This is my first ever coding project. I am self taught, so I will be happy for any help.
This is me trying to build my idea of a blockchain from scratch

This bit of code will create a file called "hashlist.txt" and start producing hashes based on the preset algo.

The idea here is to use the hashes as part of the trasaction section within the blockchain.
This way, each hash will represent a single coin on the chain and thus gives some value to the coin based on the PoW concept.

<h3>Getting up and running</h3>
This code runs on Python3 and requires two libraries.

- hashlib
- pathlib

These libraries can be installed using the pip3

To run the code, simply run main.py using python. The system will start checking for files and will produce hashes as instructed.

<h3>Changing the hashing algorithm</h3>
To adjust the hashing algo, please edit gethash.py
The hasing algo used is:
thehash = sha256(f'{x*y}'.encode()).hexdigest()

By changing the {x*y} new hashes will be produced.
Please make sure that the geni_hash in "filecheck.py" is update if the algo is changed.
The geni_hash is the first hash that is produces for the blockchain and has to be manually entered for now.

<h3>Mining Mode</h3>
In main.py, there is a variable "mining_mode". Flipping this bit to 1 will continue producing hashes until the code is manually stopped.
Flipping the "mining_mode" bit to 0, will produce only a single new hash.

<h3>Developer Mode</h3>
In main.py, there is a variable "devmode". Flipping this bit to 1 will erase the current "hashfile" and "blockchain" files. The code will give you a prompt where it will ask you to confirm that you want to remove the files, so please read the console output very carefully and follow the instructions. To disable devmode, flip the bit to 0.

Enjoy the code and let me know if there is anything you think I can change.
