from peewee import PrimaryKeyField, CharField

from Models.Base import BaseModel

class Roles(BaseModel):
    id = PrimaryKeyField()
    role = CharField()