"""
Módulo de filtros para acondicionar los datos para cargar la base de datos de personas en formato [Nombre,Apellido,Año,Mes,Día]
"""

def filter_final(s):
    """
    Recibe un string, elimina todos los signos no-alfanuméricos del final
    :return: Retorna el string "limpio"
    """
    counter = 0
    for i in range(len(s)-1,-1,-1):
        if not s[i].isalnum(): 
            counter += 1 # cuenta la cantidad de los signos no-alfanuméricos en el final
        else:
            break
    s = s[0:len(s)-counter] # acorta el string a esta cantidad de caracteres   
    return s    


def filter_initial(s):
    """
    Recibe un string, elimina todos los signos no-alfanuméricos del inico
    :return: Retorna el string "limpio"
    """
    counter = 0
    for c in s:
        if not c.isalnum():
            counter += 1 # cuenta la cantidad de los signos no-alfanuméricos en el inicio
        else:
            break
    s = s[counter:len(s)] # acorta el string a esta cantidad de caracteres      
    return s   


def empty_lines_filter(list):    
    """
    Recibe una lista de listas, elimina todas las listas internas que tienen sólo elementos vacíos
    :return: Retorna la lista liberada del contenido sin sentido
    """
    for line in list:             
        counter = 0
        for item in line:
            if len(item) == 0:
                counter += 1 # cuenta la cantidad de elementos vacíos
        if len(line) == counter: # si todos son vacíos
            list.remove(line) # elimina todo el bloque
    return list 


def date_num_filter(list):    
    """
    Recibe una lista de listas, comprueba que todos los bloques contienen 5 elementos y que los tres últomos tienen solo números
    :return: Retorna la lista comprobada o la lista vacía y declara un error
    """
    for line in list:
        if len(line) != 5: # si todos los bloques contienenen 5 elementos
            print("Error del archivo")
            return [] 
        if not(line[2].isnumeric() and line[3].isnumeric() and line[4].isnumeric()):
            print("Error del archivo") # si los tres últomos elementos de cada bloque contienen solo números
            return [] 
        else:
            continue
    return list


def list_filers(list): 
    """
    Recibe una lista de listas, analiza los posibles errores, unos arregla, otros declara
    :return: Retorna la lista comprobada o la lista vacía y declara un error
    """
    for line in list: 
        for i in range(len(line)): 
            line[i] = filter_initial(line[i])
            line[i] = filter_final(line[i])
    list = empty_lines_filter(list)
    print(list)
    list = date_num_filter(list)
    print(list)
    return list
