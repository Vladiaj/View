from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Аторизация")
root.geometry("250x200")

# Проверка пользователя, что он есть в системе

# def auth(Login, password):
#     if UserController.auth(Login, password):
#         label['text'] = 'Вы успешно авторизировались'
#         PanelDispetcera.mainloop()
#     else:
#         label['text'] = 'Неправильный пароль или логин'

# Логин и заполнение для поля Логина

LabelLogin = Label(text="Введите Логин")
EnterLogin = Entry()

LabelLogin.pack(anchor=CENTER)
EnterLogin.pack(anchor=CENTER)

# Пароль и заполнение для поля Пароля

LabelPassword = Label(text="Введите Логин")
EnterPassword = Entry(show='*')

LabelPassword.pack(anchor = CENTER)
EnterPassword.pack(anchor = CENTER)

label = Label()
label.pack(anchor = CENTER)

#Кнопка

button_auth =Button(text="Вход",background='red',foreground='black')
                        # command=lambda: auth(EnterLogin.get(), EnterPassword.get()))
button_auth.pack(anchor="center")

if __name__ == "__main__":
    root.mainloop()