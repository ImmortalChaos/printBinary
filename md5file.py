#-*-encoding=utf-8-*-
import sys
import hashlib

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

if __name__ == "__main__" :
    print md5sum(sys.argv[1])