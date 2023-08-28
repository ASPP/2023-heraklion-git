import json
import getpass
import os

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb(username, password):
    if os.path.exists(PATH):
        pwdb={}
        with open(PATH, "rt") as f:
            pwdb = json.load(f)
        authenticate(username, password, pwdb)    
    else:
        pwdb=add_user(username, password, pwdb={})
        write_pwdb(pwdb)
        print("First user added!")
    return pwdb


def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        f.write(json.dumps(pwdb))
        f.write("\n")
    f.close()


def authenticate(username, password, pwdb):
    if username in pwdb:
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong password")
    else:
        pwdb = add_user(username, password, pwdb)
        write_pwdb(pwdb)
        print("New user added")

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb(username, password)

