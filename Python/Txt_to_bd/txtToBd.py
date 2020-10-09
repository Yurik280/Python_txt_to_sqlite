"""  
    Yury Panov
    09-oct-2020
    Versión 1
"""

import sqlite3
import codecs # para tratar archivos con símbolos especiales de UTF-8
from os import system
system("cls")

#Constantas:
fileName = "personal.txt"
dbName = "personal.db"

def main():
    dataList = extractData(fileName)
    chargeDb(dataList, dbName)


def extractData(fileName):
    """  
    recibe el nombre del archivo de texo con datos en formato:
    Nombre,Apellido,Año,Mes,Día, separados con "\n"
    :return: retorna una lista de listas con strings de datos
    """
    try:        
        with codecs.open(fileName, "r", encoding='utf8') as f: # abrir el archivo codificado en UTF-8
            file = f.read()
        if file[len(file)-1:len(file)] == "\n":
            file = file[0:len(file)-2] # eliminar el "\n" final, si lo hay
        dataList = file.split("\n") # genera una lista de lineas
        newDataList=[]
        for line in dataList:
            line = line[0:len(line)-1] # eliminar la coma final
            newLine = line.split(",") # genera la lista de datos
            newDataList.append(newLine) # junta la lista de datos a la lista general
        return newDataList
    except:
        print("No se puede encontrar el archivo")
        return []

def chargeDb(dataList, dbName):
    """
    Recibe una lista de listas con strings de datos y el nombre de la base de datos
    en formato: [Nombre,Apellido,Año,Mes,Día]
    Crea una base de datos con el nombre indicado y carga los datos 
    """
    con=sqlite3.connect(dbName) # conexión
    cursor=con.cursor() # cursor
    cursor.execute("""CREATE TABLE IF NOT EXISTS PERSONAS ( 
        Nombre text, 
        Apellido text, 
        Year integer,
        Month integer,
        Day integer	
        )""")
    con.commit()
    try:
        for i in range(len(dataList)):
            cursor.execute("INSERT INTO PERSONAS VALUES (?,?,?,?,?)",(dataList[i])) # inserta datos
            con.commit()
        print("Los datos se cargaron con éxito")
    except:
        print("Error del archivo")    
    con.close() # cierra la conexión

main()