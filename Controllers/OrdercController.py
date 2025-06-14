from Controllers.ClientController import ClientController
from Controllers.DeliveryController import DeliveryController
from Controllers.CurierController import CurierController
from Models.order import *

class OrderControllers:

    def get(cls):
        return Orders.select().execute()

    @classmethod
    def update_status(cls, id_order):
        Orders.update({Orders.status:True}).where(Orders.id==id_order).execute()

    @classmethod
    def add(cls, id_user_CL, id_user_CU, item_id, endData, address):
        Orders.create(id_user_CL=id_user_CL, id_user_CU=id_user_CU, item_id=item_id, endData=endData, address=address)

    @classmethod
    def update_all(cls, id, **fields):
        for key, value in fields.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def delete(cls, id):
        Orders.delete().where(Orders.id == id).execute()

    @classmethod
    def get_one(cls, id):
        return Orders.get(Orders.id == id)


if __name__ == "__main__":

    ord = OrderControllers()



    OrderControllers.add('TEST','name')


    # OrderControllers.update_status(1)
    for row in ord.get():
        print(row.client_id.name, row.delivery_id.name, row.status)