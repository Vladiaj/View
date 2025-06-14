from cProfile import label
from itertools import count
from tkinter import *
from tkinter import ttk

from Controllers.ClientController import ClientController
from Controllers.DeliveryController import DeliveryController
from Controllers.OrdercController import OrderControllers
from Controllers.userController import UserController
from Models.client import Client
from Models.order import Orders
from Models.users import Users
from main2 import columns


def autorization():
    def auth(Login, password):
        if UserController.auth(Login, password):
            window_succes = Toplevel()
            window_succes.title("Успех")
            window_succes.geometry("400x100")
            success_auth = Label(window_succes, text="Добро пожаловать")
            success_auth.pack(side=TOP)
            close_button = ttk.Button(window_succes, text="Закрыть окно", command= lambda: [auth_role_id(Login)])
            close_button.pack(anchor="center", expand=1)

        else:
            window_fail = Toplevel()
            window_fail.title("Ошибка")
            window_fail.geometry("400x100")
            fail_auth = Label(window_fail, text="Вы ввели неправильный пароль или логин")
            fail_auth.pack(side = TOP)
            close_button = ttk.Button(window_fail, text="Закрыть окно", command=lambda: window_fail.destroy())
            close_button.pack(anchor="center", expand=1)

        def auth_role_id(Login):

            if UserController.get_role(Login).role_id.id == 2:
                panel_Auth.destroy()
                panel_operator()


            elif UserController.get_role(Login).role_id.id == 1:
                panel_Auth.destroy()
                panel_admin()



    panel_Auth = Tk()
    panel_Auth.geometry("480x300")
    panel_Auth.title("Авторизация")

    title_window = Label(panel_Auth, text="Авторизация", font=('Times New Roman', 16), height=3)
    title_window.pack(side=TOP)

    input_login = Entry(panel_Auth, width=50)
    name_input_login = Label(panel_Auth, text='Введите Логин')
    name_input_login.pack(anchor="center", pady=5)
    input_login.pack(anchor="center", pady=5)

    input_password = Entry(panel_Auth, width=50)
    name_input_login = Label(panel_Auth, text='Введите Пароль')
    name_input_login.pack(anchor="center", pady=5)
    input_password.pack(anchor="center", pady=5)

    button_auth = Button(panel_Auth, text="Вход",
                         height=5,
                         width=10,
                         background='green',
                         foreground='black',
                         command=lambda: auth(input_login.get(), input_password.get()))
    button_auth.pack(anchor="center", pady=5)

    panel_Auth.mainloop()


def panel_admin():

    def update_user():
        update_user_panel = Toplevel()
        update_user_panel.geometry("500x700")
        update_user_panel.title("Обновление Данных Пользователя")


    def get_users(x):
        User = UserController()
        for row in User.get():
            x.append([row.id,row.login, row.password,row.role_id, row.fullname,row.archive])


    def add_user():
        add_user_panel = Toplevel()
        add_user_panel.geometry("500x700")
        add_user_panel.title("Добавление пользователя")

        New_user_name = Entry(add_user_panel, width=50)
        New_user_name_label = Label(add_user_panel, text="Полное имя пользователя")
        New_user_name_label.pack(anchor='center', pady=5)
        New_user_name.pack(anchor='center', pady=5)

        new_user_login = Entry(add_user_panel, width=50)
        new_user_login_label= Label(add_user_panel, text = "Логин Пользователя")
        new_user_login_label.pack(anchor='center', pady=5)
        new_user_login.pack(anchor='center', pady=5)

        new_user_password = Entry(add_user_panel, width=50)
        new_user_password_label = Label(add_user_panel,text="Пароль Пользователя")
        new_user_password_label.pack(anchor='center', pady=5)
        new_user_password.pack(anchor='center', pady=5)

        new_user_role = Entry(add_user_panel, width=50)
        new_user_role_label = Label(add_user_panel, text="Роль пользователя")
        new_user_role_label.pack(anchor='center', pady=5)
        new_user_role.pack(anchor='center', pady=5)

        button_add_user = Button(add_user_panel,
                                 text="Добавить",
                                 width=8,
                                 background='red',
                                 foreground='white',
                                 command=lambda :UserController.add(new_user_login.get(),new_user_password.get(),new_user_role.get(),New_user_name.get()))
        button_add_user.pack(anchor='s')
        


    panel_net = Tk()
    panel_net.geometry("900x700")
    admin_title = Label(panel_net, text="Панель Администратора", font=('Times New Roman', 16), height= 3)
    # admin_title.grid(column=0, row=0, columnspan=12, padx=330, pady=10)
    admin_title.pack(anchor = 'n')

    #Список пользователей

    title_list_users_admin = Label(panel_net, text="Список пользователей", font=('Times New Roman',16), height=3)
    # title_list_users_admin.grid(column=0, row=1, columnspan=12, padx=330, pady=10)
    title_list_users_admin.pack(anchor = 'center')


    user=[]
    get_users(user)
    columns=("id",'login','password','role_id','fullname','archive')

    tree= ttk.Treeview(columns=columns, show='headings')
    tree.pack(fill=BOTH, expand=1)

    tree.heading("id", text="ID",anchor=W)
    tree.heading('login', text='login', anchor=W)
    tree.heading('password', text='password', anchor=W)
    tree.heading('role_id', text='role_id', anchor=W)
    tree.heading('fullname', text='fullname', anchor=W)
    tree.heading('archive', text='archive', anchor=W)

    tree.column('#1',stretch=NO, width=70)
    tree.column('#2',stretch=YES, width=70)
    tree.column('#3',stretch=YES, width=70)
    tree.column('#4',stretch=NO, width=70)
    tree.column('#5',stretch=YES, width=70)
    tree.column('#6',stretch=NO, width=70)

    for person in user:
        tree.insert("", END, values=person)
    #Обозначения Списка

    # title_id_user = Label(panel_net, text="ID")
    # title_id_user.grid(column=0, row=2)
    #
    # title_login_user = Label(panel_net,text="LOGIN")
    # title_login_user.grid(column=1, row=2)
    #
    # title_password_user = Label(panel_net, text="PASSWORD")
    # title_password_user.grid(column=2, row=2)
    #
    # title_role_id_user = Label(panel_net, text="ROLE ID")
    # title_role_id_user.grid(column=3, row=2)
    #
    # title_fullname_user = Label(panel_net, text="FULLNAME")
    # title_fullname_user.grid(column=4, row=2)
    #
    # title_archive_user = Label(panel_net, text="ARCHIVE STATUS")
    # title_archive_user.grid(column=5, row=2)
    #
    # user = UserController
    # all_users = user.get()
    # count_row = 3
    # for row in all_users:
    #     if row.archive == 0:
    #         id_user= Label(panel_net, text=row.id)
    #         id_user.grid(column = 0, row = count_row, padx = 0, pady= 1)
    #
    #         login_user= Label(panel_net, text=row.login)
    #         login_user.grid(column = 1, row = count_row, padx = 0, pady= 1)
    #
    #         password_user = Label(panel_net, text=row.password)
    #         password_user.grid(column = 2, row = count_row, padx = 0, pady= 1)
    #
    #         role_id_user= Label(panel_net, text=row.role_id)
    #         role_id_user.grid(column = 3, row = count_row, padx = 0, pady= 1)
    #
    #         fullname_user = Label(panel_net, text=row.fullname)
    #         fullname_user.grid(column = 4, row = count_row, padx = 0, pady= 1)
    #
    #         archive_user= Label(panel_net, text=row.archive)
    #         archive_user.grid(column = 5, row = count_row, padx = 0, pady= 1)
    #
    #         button_update= Button(panel_net,
    #                               text= "Изменить",
    #                               width=8,
    #                               background='red',
    #                               foreground='white',
    #                               command = lambda login = row.login:[update_user()]
    #                               )
    #         button_update.grid(column = 6, row = count_row, padx = 0, pady= 1)
    #
    #     else:
    #         pass
    #
    #     count_row+=1
    #
    button_add_user = Button(panel_net,
                             text="Добавить",
                             width=8,
                             background='black',
                             foreground='white',
                             command= lambda : add_user())

    # button_add_user.grid(column =6, row = 2, padx = 0, pady= 1)
    button_add_user.pack(anchor = 'se')
def panel_operator():
    def add__addOrder(name, phone, adress,email, item_name,item_addres,description, item_count):
        ClientController.addClient(name,phone,adress,email)
        DeliveryController.add(item_name,item_addres,description,item_count)
        OrderControllers.add(name,item_name)
        Succes_new_order= Toplevel()
        Succes_new_order.title("Добавлен Заказ")
        Succes_new_order.geometry("400x300")
        text_1= Label(Succes_new_order, text="Заказ Добавлен. Обновите список", font=('Times New Roman', 16),
                                height=3)
        text_1.pack(side=TOP)

    def update():
        panel_order.destroy()
        panel_operator()

    def update_order():
        update_user_panel = Toplevel()
        update_user_panel.geometry("500x700")
        update_user_panel.title("Обновление Данных Заказа")

        input_client_id = Entry(update_user_panel, width=50)
        name_input_client_i = Label(update_user_panel, text="Введите Новое ID Клиента")
        name_input_client_i.pack(anchor="center", pady=5)
        input_client_id.pack(anchor="center", pady=5)

        input_curier_id = Entry(update_user_panel, width=50)
        name_input_curier_id = Label(update_user_panel, text="Введите Новое ID Курьера")
        name_input_curier_id.pack(anchor="center", pady=5)
        input_curier_id.pack(anchor="center", pady=5)

        input_delivery_name = Entry(update_user_panel, width=50)
        name_input_delivery_name = Label(update_user_panel, text="Введите ID Доставки")
        name_input_delivery_name.pack(anchor="center", pady=5)
        input_delivery_name.pack(anchor="center", pady=5)



    def add_order():


        window_add_order = Toplevel()
        window_add_order.title("Добавление нового заказа")
        window_add_order.geometry("900x700")
        add_order_title = Label(window_add_order, text="Добавление нового заказа", font=('Times New Roman', 16),
                                height=3)
        add_order_title.pack(side=TOP)

        # Клиент
        input_client_name = Entry(window_add_order, width=50)
        name_input_client_name = Label(window_add_order, text="Введите имя клиента")
        name_input_client_name.pack(anchor="center", pady=5)
        input_client_name.pack(anchor="center", pady=5)

        input_client_phone = Entry(window_add_order, width=50)
        name_input_client_phone = Label(window_add_order, text="Введите телефон клиента")
        name_input_client_phone.pack(anchor="center", pady=5)
        input_client_phone.pack(anchor="center", pady=5)

        input_client_adress = Entry(window_add_order, width=50)
        name_input_client_adress = Label(window_add_order, text="Введите адрес клиента")
        name_input_client_adress.pack(anchor="center", pady=5)
        input_client_adress.pack(anchor="center", pady=5)

        input_client_email = Entry(window_add_order, width=50)
        name_input_client_email = Label(window_add_order, text="Введите телефон клиента")
        name_input_client_email.pack(anchor="center", pady=5)
        input_client_email.pack(anchor="center", pady=5)

        # Доставка

        input_delivery_name = Entry(window_add_order, width=50)
        name_input_delivery_name = Label(window_add_order, text="Введите имя доставки")
        name_input_delivery_name.pack(anchor="center", pady=5)
        input_delivery_name.pack(anchor="center", pady=5)

        input_delivery_adress = Entry(window_add_order, width=50)
        name_input_delivery_adress = Label(window_add_order, text="Введите адрес доставки")
        name_input_delivery_adress.pack(anchor="center", pady=5)
        input_delivery_adress.pack(anchor="center", pady=5)

        input_delivery_description = Entry(window_add_order, width=50)
        name_input_delivery_description= Label(window_add_order, text="Введите описание предмета")
        name_input_delivery_description.pack(anchor="center", pady=5)
        input_delivery_description.pack(anchor="center", pady=5)

        input_delivery_count = Entry(window_add_order, width=50)
        name_input_delivery_count = Label(window_add_order, text="Введите количество предметов")
        name_input_delivery_count.pack(anchor="center", pady=5)
        input_delivery_count.pack(anchor="center", pady=5)

        btn_back = Button(window_add_order, text="Вернуться назад",
                          width=30,
                          background='green',
                          foreground='black',
                          command=lambda: window_add_order.destroy())
        btn_back.pack(side=BOTTOM)
        btn_add_order = Button(window_add_order, text="Добавить заказ",
                               width=30,
                               background='green',
                               foreground='black',
                               command= lambda :add__addOrder(input_client_name.get(),input_client_phone.get(),input_delivery_adress.get(),input_client_email.get(),input_delivery_name.get(),input_delivery_adress.get(),input_delivery_description.get(),input_delivery_count.get()))
        btn_add_order.pack(side=BOTTOM)


    panel_order = Tk()
    panel_order.geometry("900x700")
    panel_order.title("Панель Оператора")


    title_orders = Label(panel_order, text="Список действующих заказов",font=('Times New Roman',14))
    title_orders.grid(column=0, row=0, columnspan=6, padx=330, pady=10)

    # Список действующих заказов:
    title_id = Label(panel_order, text="ID")
    title_id.grid(column=0, row=1)

    title_NAME = Label(panel_order, text="NAME_CLIENT")
    title_NAME.grid(column=1, row=1)

    title_DELIVERY_ID = Label(panel_order, text="DELIVERY_ID")
    title_DELIVERY_ID.grid(column=2, row=1)

    title_CURIER = Label(panel_order, text="CURIER_ID")
    title_CURIER.grid(column=3, row=1)
    order = OrderControllers()
    list_orders = order.get()
    count_row=2

    # users = []
    #
    # User = UserController()
    # for row in User.get():
    #     users.append([row.id,row.])
    for row in list_orders:

        if row.status == 0:
            id_title = Label(panel_order, text=row.id)
            id_title.grid(column = 0, row = count_row, padx = 0, pady= 1)

            name_cluent_title = Label(panel_order, text=row.client_id.name)
            name_cluent_title.grid(column = 1, row = count_row, padx = 0, pady= 1)

            name_delivery_title = Label(panel_order, text=row.delivery_id.name)
            name_delivery_title.grid(column = 2, row = count_row, padx = 0, pady= 1)

            name_curier_title = Label(panel_order, text=row.curier_id.name)
            name_curier_title.grid(column = 3, row = count_row, padx = 0, pady= 1)

            button_update= Button(panel_order,
                                  text= "Изменить",
                                  width=8,
                                  background='red',
                                  foreground='white',
                                  command = lambda login = row.client_id:[update_order()]
                                  )
            button_update.grid(column = 4, row = count_row, padx = 0, pady= 1)
        else:
            pass

        count_row+=1


    button_add_order = Button(panel_order, text="Добавить новый заказ",
                              height=2,
                              width=15,
                              background='green',
                              foreground='black',
                              command= lambda: [add_order()])

    button_add_order.grid(column =4, row=1, padx = 0, pady= 1)
    button_update = Button(panel_order, text="Обновить",
                           height=2,
                           width=15,
                           background='green',
                           foreground='black',
                           command=lambda: update()
                           )
    button_update.grid(column=5,row=1,padx = 0, pady= 1)
    panel_order.mainloop()


autorization()
# panel_operator()