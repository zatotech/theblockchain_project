import gethash
import testhash
import filecheck

x = 1
y = 0
st = 0
mining_mode = 1

found_hash, found_y, found_x = gethash.newhash(y,x)

filecheck.check_if_file_is()

if (mining_mode):
    while 1:
        rx, ry, st = testhash.test_hash(found_hash, found_y, found_x)
        found_hash, found_y, found_x = gethash.newhash(ry, rx)
else:
    while st == 0:
        rx, ry, st = testhash.test_hash(found_hash, found_y, found_x)
        found_hash, found_y, found_x = gethash.newhash(ry, rx)