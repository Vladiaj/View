from tkinter import *
from tkinter import ttk
OrderControlle = [(1,212,'r','re','ew','Сейчас','Тоже сейчас')]
PanelMessage = Tk()
PanelMessage.title("Панель Сообщений")
PanelMessage.geometry("1000x500")

# определяем данные для отображения
people = []

# определяем столбцы
columns = ("id","Number_phone","Name_client","cause","role")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определяем заголовки
tree.heading("id", text="ID")
tree.heading("Number_phone", text="Номер")
tree.heading("Name", text="Имя")
tree.heading("cause", text="Причина")
tree.heading("role", text="Пользователь")


# добавляем данные
for OrderController in people:
    tree.insert("", END, values=OrderController)

# Кнопка Выхода
Button_Exit = Button(text='Выход',
                     command= lambda :(PanelMessage.destroy(),PanelDispetcera()))
Button_Exit.pack(anchor = SW)

# Кнопка для ответа
button_archive = Button(text='Архив',
                        command= lambda :(PanelMessage.destroy(),PanelMessage()))
button_archive.pack(anchor = SE)

if __name__ == "__main__":
    PanelMessage.mainloop()