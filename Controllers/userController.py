from select import select
from tkinter.messagebox import RETRY
from venv import create
from bcrypt import hashpw, gensalt, checkpw
from setuptools.package_index import user_agent

from Models.users import *
class UserController:


    @classmethod
    def get(cls):
        return Users.select().execute()

    @classmethod
    def auth(cls, login, password):
        user = Users.get_or_none(Users.login == login)
        if user is not None:
            if user.password == password:
                return user
            else:
                return False
        else:
            return False

    @classmethod
    def add(cls, login, password, role_id, fullname, Auto, NumberPhone):
        Users.create(login=login, password=password, role_id=role_id, fullname=fullname, Auto, NumberPhone)

    @classmethod
    def auth_user(cls,login,password):
        if Users.get_or_none(Users.login == login) != None:
            pawd = Users.get_or_none(Users.login==login).password
            if checkpw(password.encode('utf-8'),pawd.encode('utf-8')):
                return True
        return False

    @classmethod
    def update_all(cls, id, **fields):
        for key, value in fields.items():
            Users.update({key: value}).where(Users.id == id).execute()

# if __name__ == "__main__":
#
