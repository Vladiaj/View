from tkinter import *
from tkinter import ttk
OrderControlle = [(1,212,'r','re','ew','Сейчас','Тоже сейчас')]
PanelDispetcera = ()
panel_curier = Tk()
panel_curier.title("Панель Диспетчера")
panel_curier.geometry("1000x500")

# определяем данные для отображения
people = []

# определяем столбцы
columns = ("id","Name","car","id_order","status")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определяем заголовки
tree.heading("id", text="ID")
tree.heading("Name", text="Имя")
tree.heading("car", text="Транспорт")
tree.heading("id_order", text="Заказ")
tree.heading("status", text="В сети")

# добавляем данные
for OrderController in people:
    tree.insert("", END, values=OrderController)

# Кнопка в Архав
button_archive = Button(text='Архив',
                        command= lambda :(panel_curier.destroy(),PanelDispetcera()))
button_archive.pack(anchor = SW)
if __name__ == "__main__":
    panel_curier.mainloop()