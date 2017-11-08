#!/usr/bin/python3

# Galen Michael Helfter
# ghelfter@gmail.com
# ghelfter@protonmail.com
# login.py

# Password retrieval header
from getpass import getpass

# Steampy headers
from steampy.client import SteamClient

# Global steam client variable
steam_client = None

# Read the username in
def read_username():
    print("Enter your username:")
    return input()

# Prompt and function for reading the password in
def read_password():
    return getpass("Now enter your password: ")

# Function to return our client for use in other modules
def get_client():
    return steam_client

# Initialization function
def user_login_init(key):
   steam_client = SteamClient(key)

# Log in to the account
def user_login(username, password, steamguard):
    steam_client.login(username, password, steamguard)

# Log out
def user_logout():
    steam_client.logout()
