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

def write_pwdb(username, password):
    pwdb = {username: password}
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, password, pwdb):
    if username in pwdb:
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")


username, password = get_credentials()
write_pwdb(username, password)
pwdb = read_pwdb()
authenticate(username, password, pwdb)

