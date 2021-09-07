# https://dev.to/natec425/inspecting-function-annotations-in-python-1hfd

import inspect

users = [
    {"username": "john", "password": "123456"},
    {"username": "loen", "password": "123456"},
    {"username": "smith", "password": "123456"},
]


def login(username: str, password: str) -> bool:
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("You Are Logged In")
            return True
    return False


login_sig = inspect.signature(login)
print(login_sig)
usrname = login_sig.parameters["username"]
pwd = login_sig.parameters["password"]
print(usrname)  # username: str
print(pwd)  # password: str

print(usrname.annotation)  # <class 'str'>
print(pwd.annotation)  # <class 'str'>
print(login_sig.return_annotation)  # <class 'bool'>
