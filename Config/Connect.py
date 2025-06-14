from peewee import *
import pymysql
mysql_db = MySQLDatabase(  'SHiV1234_food', user= 'SHiV1234_adm_c', password = '111111', host = '10.11.13.118', port =3306)

def connect_db():

    mysql_db=MySQLDatabase('SHiV1234_food',
                    user='SHiV1234_adm_c',
                  password='111111',
                  host='10.11.13.118',
                  port=3306)
    return mysql_db


if __name__ == "__main__":
    try:
        connect_db().connect()
        print("Успешное подключение")
    except OperationalError as error:
        print( f"Ошибка, {error}")