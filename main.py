#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# main.py

import sys

def main(argv):
    # Note: This will be one element smaller than the argc of a C program,
    # since it will not include the program name after being filtered through
    # the main calling 'if' statement.
    argc = len(argv)
    print("Doing nothing")

if __name__ == "__main__":
    main(sys.argv[1:])
