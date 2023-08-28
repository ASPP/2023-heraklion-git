import json
import getpass
import hashlib
import os
PATH = "./pwdb.json"
max_tries = 3



def get_username():
    return input("Username: ")

def get_password():
    return getpass.getpass("Password: ")


def read_pwdb():
    with open(PATH, "rt") as f:
        pwdb = json.load(f)
    return pwdb

def write_pwdb(pwdb):
    with open(PATH, "w") as f:
        json.dump(pwdb, f)


def authenticate(username, pwdb):
    for i in range(max_tries):
        if hash(username,get_password()) == pwdb[username]:
            print("Successfully authenticated!")
            break
        else:
            print("Wrong password, try again")

def hash(username,password):
    salted = username + password
    return hashlib.md5(salted.encode()).hexdigest()


def add_user(username, password, pwdb):
    pwdb[username] = password
    return pwdb


def database_exists():
    if not os.path.exists(PATH):
        d = dict()
        with open(PATH,'w') as f:
            json.dump(d,f)
    else:
        with open(PATH,'r+') as f:
            d = json.load(f)
    return d


def run():
    database = database_exists()
    username = get_username()

    if username in database:
        authenticate(username,database)
    else:
        if input('Username does not exist create new account?[Y,N]') == 'Y':
            p = hash(username,get_password())
            print('repeat new password')
            i = 0
            for i in range(10):
                if hash(username,get_password()) == p:
                    database[username] = p
                    write_pwdb(database)
                    break
                else:
                    print("wrong password, work on your shortterm memory please!")

    


if __name__ == "__main__":
    run()