#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# main.py

import sys

import login

# Steampy functions

# Global variables
username = None
password = None

def main(argv):
    # Note: This will be one element smaller than the argc of a C program,
    # since it will not include the program name after being filtered through
    # the main calling 'if' statement.
    argc = len(argv)

    # Steam login
    username = login.read_username()

    password = login.read_password()

    # Try logging in, exit on failure
    #try:
    #    login.
    #except:
    #    sys.stderr.write("Error, login failed. Exiting...")
    #    # Exit with an error code
    #    sys.exit(1)

    # After logging in, clear password back to none
    password = None

if __name__ == "__main__":
    main(sys.argv[1:])
