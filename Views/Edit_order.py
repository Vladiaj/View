from tkinter import *
from tkinter import ttk

order_Edit = Tk()
order_Edit.title("Изменение заказа")
order_Edit.geometry("1000x500")

label = Label(text="Изменение заказа")
label.grid(columnspan =4, column=1, row =0, padx = 500)
# Изменнение номера
newNumber = Label(text= "Новый номер телефона")
newNumber.grid(column=1, row=1)

newEnterNumber = Entry()
newEnterNumber.grid(column=1, row=2)
# Изменени клиента
newClient = Label(text= "Новый клиент")
newClient.grid(column=1, row=3)

newEnterClient = Entry()
newEnterClient.grid(column=1, row=4)
# Изменение Товара
newItem = Label(text= "Новый товар")
newItem.grid(column=1, row=5)

newEnterItem = Entry()
newEnterItem.grid(column=1, row=6)
# Изменение старта
newStartData = Label(text= "Новая дата начало заказа")
newStartData.grid(column=1, row=7)

newEnterStartData = Entry()
newEnterStartData.grid(column=1, row=8)
# Изменение Конец
newEndData = Label(text= "Новая дата окончание заказа")
newEndData.grid(column=1, row=9)

newEnterEndData = Entry()
newEnterEndData.grid(column=1, row=10)

# ID заказа

labelid= Label(text="Введите ID заказа")
labelid.grid(column =1, row=11)

# # Кнопка для изменения yjvthf
#
# button_edit_phone = Button(text="Обновить данные телефона",
#                      command= lambda : clientCpntroller.update_all(labelId.get(),phone = newNumber.get))
# button_edit_phone.grid(column=2, row =2)
#
# #
# button_edit_client = Button(text="Обновить имя клиента",
#                      command= lambda : clientCpntroller.update_all(labelId.get(),name = newClient.get))
# button_edit_client.grid(column=2, row =4)
#
# # Кнопка для обновления товара
# button_edit_item = Button(text="Обновить товар",
#                      command= lambda : itemController.update_all(labelId.get(),name = newItem.get))
# button_edit_item.grid(column=2, row =6)
#
# # Кнпока для обновления началы даты
# button_edit_startOrder = Button(text="Обновить дату начало заказа",
#                      command= lambda : orderController.update_all(labelId.get(),dataStart = newStartData.get))
# button_edit_startOrder.grid(column=2, row =8)
#
# # Кнопка для обновления окончания даты
# button_edit_endOrder = Button(text="Обновить дату окончания заказа",
#                      command= lambda : orderController.update_all(labelId.get(),dataEnd = newEndData.get))
# button_edit_endOrder.grid(column=2, row =10)

if __name__ == "__main__":
    order_Edit.mainloop()