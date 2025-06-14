from Models.Base import *
from Models.client import *
from Models.Delivery import *
from Models.curier import *

class Orders(BaseModel):
    id = PrimaryKeyField()
    id_user_CL = ForeignKeyField(Users)
    id_user_CU = ForeignKeyField(Users)
    item_id = ForeignKeyField(Item)
    startData = DateTimeField(default=datetime.now())
    endData = DateTimeField()
    archive = BooleanField(default=False)
    address = CharField()
