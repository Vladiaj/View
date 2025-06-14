from peewee import PrimaryKeyField, CharField, ForeignKeyField, BooleanField

from Models.Base import BaseModel
from Models.roles import Roles

class Users(BaseModel):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    role_id = ForeignKeyField(Roles)
    fullname = CharField()
    archive = BooleanField()