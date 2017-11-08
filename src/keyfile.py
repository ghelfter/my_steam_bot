#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# keyfile.py

def read_keyfile(fpath):
    rval = None            # Return key value
    fd = open(fpath, "r")
    count = 0

    for line in fd:
        line = line.strip()
        if not line:
            continue
        if count == 0:
            rval = line
            count = 1
            
        # We only read the first line of the file
        else:
            continue

    return rval
