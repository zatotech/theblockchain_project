import pathlib

geni_hash = "114bd151f8fb0c58642d2170da4ae7d7c57977260ac2cc8905306cab6b2acabc"

def check_if_file_is():
    file = pathlib.Path('hashlist.txt')
    if (file.exists() == False):
        file.touch()
        f = open(file, "w")
        f.write(geni_hash+"\n")
        f.close()

