from tkinter import *
from tkinter import ttk
OrderControlle = [(1,212,'r','re','ew','Сейчас','Тоже сейчас')]
PanelDispetcera = Tk()
PanelDispetcera.title("Панель Диспетчера")
PanelDispetcera.geometry("1000x500")

# определяем данные для отображения
people = []

# определяем столбцы
columns = ("id","Number_phone","Curier","Name_client","Item","Start_order", "End_order")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определяем заголовки
tree.heading("id", text="ID")
tree.heading("Number_phone", text="Номер")
tree.heading("Curier", text="Курьер")
tree.heading("Name_client", text="Клиент")
tree.heading("Item", text="Товар")
tree.heading("Start_order", text="Начало")
tree.heading("End_order", text="Конец")

# добавляем данные
for OrderController in people:
    tree.insert("", END, values=OrderController)

# Кнопка Выхода
Button_Exit = Button(text='Выход',
                     command= lambda :PanelDispetcera.destroy())
Button_Exit.pack(anchor = SW)

# Кнопка в Архав
button_archive = Button(text='Архив',
                        command= lambda :(PanelDispetcera.destroy(),panel_archive()))
button_archive.pack(anchor = SE)
# Конпка в список курьеров
Button_Curier = Button(text='Курьеры',
                     command= lambda :(PanelDispetcera.destroy(),panel_curier()))
Button_Curier.pack(anchor = SE)
# Кнопка вызовов
Button_message = Button(text='Сообщения',
                     command= lambda :(PanelDispetcera.destroy(), panel_message()))
Button_message.pack(anchor = SE)

Button_edit = Button(text="Обновить заказ", command = lambda :(padel_edit_order()))
Button_edit.pack(anchor = SE)
if __name__ == "__main__":
    PanelDispetcera.mainloop()