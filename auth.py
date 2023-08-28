import json
import getpass
from pathlib import Path

PATH = "./pwdb.json"

def get_credentials():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return username, password

def read_pwdb():

    if Path(PATH).exists():
        with open(PATH, "rt") as f:
            pwdb = json.load(f)
    else:
        pwdb={'empty':'empty'}
        write_pwdb(pwdb)
    return pwdb

def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, password, pwdb):
    print(pwdb)
    if username in pwdb:
        if password == pwdb[username]:
            print("Successfully authenticated!")
        else:
            print("Wrong Password")
    else:
        print('user does not exists \n do you want to create user?')
        register=input ('Y/N\n')

        while register != 'Y' and register != 'N':
            print('invalid input only Y or N. maybe is not allowed')
            register=input ('Y/N\n')

        if register=='Y':
            pwdb = add_user(username, password, pwdb)
            write_pwdb(pwdb)
        else:
            print(" I dind't want you anyway :p")
        

def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb

username, password = get_credentials()
pwdb = read_pwdb()
authenticate(username, password, pwdb)

