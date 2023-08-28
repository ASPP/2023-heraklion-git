import json
import getpass
import hashlib
from pathlib import Path
import os

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb():
    if Path(PATH).exists():
        with open(PATH, "rt") as f:
            pwdb = json.load(f)
        return pwdb
    else:
        return {}

def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, password, pwdb):
    if username in pwdb:
        # get salt
        salt=pwdb[username][0]
        passw=pwdb[username][1]
        if pwhash(salt,password) == passw:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        pwdb = add_user(username, password, pwdb)
        write_pwdb(pwdb)

def add_user(username, password, pwdb):
    salt = get_salty()
    pwdb[username] = [salt,pwhash(salt,password)]
    return pwdb


def pwhash(salt,password: str) -> str:
     
    salted=salt + password
    return hashlib.sha256(salted.encode("utf-8")).hexdigest()

def get_salty():
    return str(os.urandom(16))
username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

