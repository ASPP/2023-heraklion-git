import json
import getpass

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
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        add_new_user = input("Add new user? [y/n]").lower()
        if add_new_user=="y":
            pwdb = add_user(username, password, pwdb)
            write_pwdb(pwdb)
        elif add_new_user=="n":
            pass
        else:
            print("Please enter y or n, idiot :)")

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)
