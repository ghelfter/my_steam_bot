#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# main.py

import sys

import login
import keyfile

# Steampy functions
from steampy.client import SteamClient

# Global variables
username = None
password = None

def print_usage():
    print("Usage: ./main.py [key_file] [steamguard_file]")

def main(argv):
    # Note: This will be one element smaller than the argc of a C program,
    # since it will not include the program name after being filtered through
    # the main calling 'if' statement.
    argc = len(argv)

    # Note: argv must contain two arguments

    # This will be changed to less than two later, when the steamguard file
    # part is implemented.
    if argc < 1:
        print("Error, wrong number of arguments.")
        print_usage()
        exit(1)

    # Try keyfile first
    try:
        key = keyfile.read_keyfile(argv[0])
    except:
        print("Error, failure to read keyfile.")
        exit(1)

    # Steam login
    username = login.read_username()
    password = login.read_password()

    # Try logging in, exit on failure
    try:
        login.user_login_init(key)
    except:
        print("Error, failed to initialize steam client.")
        sys.exit(1)

    try:
        login.user_login(username, password)
    except:
        print("Error, failed to log in.")
        sys.exit(1)

    # After logging in, clear password back to none
    password = None

    # Exit the steam client
    login.user_logout()

if __name__ == "__main__":
    main(sys.argv[1:])
