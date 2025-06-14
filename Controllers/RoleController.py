from Models.roles import *

class RoleController:
    @classmethod
    def get(cls):
        return Roles.select().execute()

    @classmethod
    def get_one(cls, id):
        return Roles.get(Roles.id == id).name

    @classmethod
    def add(cls, name):
        Roles.create(name=name)

    @classmethod
    def update(cls, id, new_name):
        Roles.update({Roles.name: new_name}).where(Roles.id == id).execute()

    @classmethod
    def delete(cls, id):
        Roles.delete().where(Roles.id==id).execute()
