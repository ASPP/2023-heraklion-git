import json
import getpass
import os

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb():
    if os.path.isfile(PATH): 
        with open(PATH, "rt") as f:
            pwdb = json.load(f)
    else:
        pwdb = {}
    return pwdb


def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)

def authenticate(username, password, pwdb):
    msg_failed = "Wrong username and/or password."
    if username in pwdb:
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print(msg_failed)
    else:
        print(msg_failed)
        if input("Register? y/n") == "y":
            username, password = get_credentials()
            pwdb = add_user(username, password, pwdb)
            write_pwdb(pwdb)

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

