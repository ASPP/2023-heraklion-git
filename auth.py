import json
import getpass
import hashlib

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb():
    with open(PATH, "rt") as f:
        pwdb = json.load(f)
    return pwdb

def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, password, pwdb):
    if username in pwdb:
        if pwhash(password) == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        pwdb = add_user(username, password, pwdb)
        write_pwdb(pwdb)

def add_user(username, password, pwdb):
    pwdb[username] = pwhash(password)
    return pwdb


def pwhash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

