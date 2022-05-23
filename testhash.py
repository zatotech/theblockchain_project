
def test_hash(hash_to_check, found_y, found_x):
    file = open("hashlist.txt", "r")
    listhash = file.readlines()
    state = 0
    for line in listhash:
        fixed_line = line.split()
        fixed_hash = hash_to_check.split()
        if (fixed_hash == fixed_line):
            #print(str(line.split()) + " is a old hash" )
            state = 0
            break
        if EOFError:
            state = 1
    file.close()
    if (state == 1):
        writingfile = open("hashlist.txt", "a")
        print("Found a new hash: " + str(hash_to_check.split()))
        print(f'The solution is y = {found_y}')
        writingfile.write(str(hash_to_check) + "\n")
        writingfile.close()
    return (found_y + 1, found_x + 1, state)
