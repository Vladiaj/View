from tkinter import *
from tkinter import ttk
OrderControlle = [(1,212,'r','re','ew','Сейчас','Тоже сейчас')]
Archive = Tk()
Archive.title("Панель Диспетчера")
Archive.geometry("1000x500")

# определяем данные для отображения
people = []

# определяем столбцы
columns = ("id","Number_phone","Curier","Name_client","Item","Start_order", "End_order", "status")

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
tree.heading("status", text="Заархированный")

# добавляем данные
for OrderController in people:
    tree.insert("", END, values=OrderController)

# Кнопка Выхода
Button_Exit = Button(text='Выход',
                     command= lambda :(Archive.destroy(), PanelDispetcera()))
Button_Exit.pack(anchor = SW)

if __name__ == "__main__":
     Archive.mainloop()