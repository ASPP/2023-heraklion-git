import json
import getpass
import hashlib
import string
import random

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
        if pwhash(pwdb[username][0]+ password) == pwdb[username][1]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        pwdb = add_user(username, password, pwdb)
        write_pwdb(pwdb)

def add_user(username, password, pwdb):
    # create the salt
    salt = make_salt()
    # concatanate the salt and the pasw
    salted_pasw=salt + password
    # get the hash out of both
    pwdb[username] = [salt, pwhash(salted_pasw)]
    return pwdb

def make_salt():
    # initializing size of string
    N   =  12 #same for every initial
    salt = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=N))
    return salt

def pwhash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

