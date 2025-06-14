from Models.item import *

class ItemController:
    @classmethod
    def get(cls):
        return Item.select().execute()

    def get_one(cls,id):
        return Item.get(Item.id==id).name

    @classmethod
    def add(cls, name):
        Item.create(name=name)

    def update(cls, id, new_name):
        Item.update({Item.name: new_name}).where(Item.id == id).execute()

    @classmethod
    def delete(cls, id):
        Item.delete().where(Item.id == id).execute()
