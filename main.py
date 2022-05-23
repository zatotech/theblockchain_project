import gethash
import testhash
import filecheck
import devmode

x = 1
y = 0
st = 0
mining_mode = 0
dev_mode = 1

if dev_mode:
    print("WARNING: Developer mode is enabled")
    print("WARNING: This will reset and remove all data")
    print("WARNING: Do you wish to continue")
    print("WARNING: Type capital yes to continue")
    continue_devmode = str(input("WARNING: Type anything else to abort mission \n"))
    if continue_devmode == "YES":
        devmode.remove_files()
    else:
        print("WARNING: Mission aborted")
        exit()

found_hash, found_y, found_x = gethash.newhash(y,x)

filecheck.check_if_file_is()

if mining_mode:
    while 1:
        rx, ry, st = testhash.test_hash(found_hash, found_y, found_x)
        found_hash, found_y, found_x = gethash.newhash(ry, rx)
else:
    while st == 0:
        rx, ry, st = testhash.test_hash(found_hash, found_y, found_x)
        found_hash, found_y, found_x = gethash.newhash(ry, rx)