"""  
    Yury Panov
    13-oct-2020
    Versión 4
"""

from datetime import date
from os import system
import sqlite3
system("cls")


#Constantas:
dbName = "personal.db"


def main():
    dateList = date_list_extract(dbName, input("Ingrese un apellido a consultar la edad: "))
    print("La edad es ", years_diff(dateList), " años")


def date_list_extract(dbName, surname):
    """  
    Extracta datos de fecha de una base de datos
    :param dbName: el nombre de la base de datos
    :param surname: el apellido a consultar
    :return: una tupla de números en formato (YYYY,mm,dd)
    """
    con = sqlite3.connect(dbName) # conexión
    cursor = con.cursor() # cursor
    cursor.execute("SELECT year, month, day FROM Personas WHERE Apellido = ?", (surname,)) # consulta los datos
    dateList = cursor.fetchall() # acumula datos en una lista de tuplas
    con.close() # cierra la conexión    
    return(dateList[0]) 

    
def years_diff(dateList):
    """  
    Calcula la cantidad de años entre la fecha de hoy y la fecha dada en el parametro    
    :param dateList: una tupla que contiene la fecha en formato: (YYYY,mm,dd)
    :return: un numero de años de diferencia
    """
    todayList = [date.today().year, date.today().month, date.today().day] # pasa los datos a una lista de números
    years_diff = todayList[0]-dateList[0] # calcula años de diferencia
    if todayList[1] < dateList[1]: # compara meses
        years_diff -= 1
    elif todayList[1] == dateList[1] and todayList[2]<dateList[2]: # compara días
        years_diff -= 1
    return years_diff	


main()
