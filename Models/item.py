from Config.Connect import *

class Item(Model):

id = PrimaryKeyField()
name = CharField()

class Meta:
    database = mysql_db
