from peewee import PrimaryKeyField, CharField, ForeignKeyField, BooleanField

from Models.Base import BaseModel
from Models.roles import Roles

class Users(BaseModel):
    id = PrimaryKeyField()
    login = CharField(unique=True, max_length=150)
    password = CharField()
    fullname = CharField()
    role_id = ForeignKeyField(Roles)
    numberPhone = IntegerField()
    Auto = CharField()
