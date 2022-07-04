import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


def gerar_cnx():
    cnx = mysql.connector.connect(
        host=os.getenv('HOST'),
        database=os.getenv('NAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT'),
    )
    return cnx

def cnx_sem_database():
    cnx = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT'),
    )
    return cnx