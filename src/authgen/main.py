#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# main.py

import sys

# Steamp functions
from steam import SteamID
from steam import SteamClient
from steam.enums.emsg import EMsg

# Global variables
username = None
password = None

def write_json(steamid, secret1, secret2):
    print("{")
    print("    steamid: " + steamid)
    print("}")

def main(argv):
    # Note: This will be one element smaller than the argc of a C program,
    # since it will not include the program name after being filtered through
    # the main calling 'if' statement.
    argc = len(argv)

    # Instantiate client
    client = SteamClient()

    client.cli_login()

    print(client.steam_id)

    # Acquire secrets

    # Exit the steam client
    client.logout()

if __name__ == "__main__":
    main(sys.argv[1:])
