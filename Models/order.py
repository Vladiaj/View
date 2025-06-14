from Models.Base import *
from Models.client import *
from Models.Delivery import *
from Models.curier import *

class Orders(BaseModel):
    id = PrimaryKeyField()
    client_id = ForeignKeyField(Client)
    delivery_id = ForeignKeyField(Delivery)
    curier_id = ForeignKeyField(Curier, default=0)
    status = BooleanField(default=0)