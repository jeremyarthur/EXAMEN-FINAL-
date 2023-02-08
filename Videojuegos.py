#Se importan csv y pandas para manejo de datos csv
import csv
import pandas as pd


#Lista que contiene los datos de videojuegos
lista_videojuegos=[]

#Clase Videojuegos
class Videojuegos:
    def __init__(self, nombre, categoria, clasificacion, precio, ventas, codigo_de_barra):
        self.nombre = nombre
        self.categoria = categoria
        self.clasificacion = clasificacion
        self.precio = precio
        self.ventas = ventas
        self.codigo_de_barra = codigo_de_barra

#Funcion que registra los datos de videojuegos
def registrar():
    print('')
    try:
        x=int(input("Indique la cantidad de videojuegos que desea registrar: "))


        for i in range(0,x):
        

            nombre = str(input("Ingrese el nombre del videojuego:"))

            sel_categoria=int(input('''Ingrese el numero de categoria del videojuego:
            1)Accion
            2)Aventura
            3)Arcade
            4)Deportes
            5)Estrategia
            6)Otros
            --->'''))

            if sel_categoria == 1:
                categoria="Accion"
            
            elif sel_categoria == 2:
                categoria = "Aventura"

            elif sel_categoria == 3:
                categoria = "Arcade"

            elif sel_categoria == 4:
                categoria = "Deportes"

            elif sel_categoria == 5:
                categoria = "Estrategia"

            elif sel_categoria == 6:
                categoria= "Otros"
            
            else:
                print("Categoria no existente")

            sel_clasificacion=int(input('''Ingrese el numero segun la clasificacion del videojuego:
            1)Clasificacion “A”: Contenido para todo el publico.
            2)Clasificacion “B”: Contenido para adolescente a partir de 12 años.
            3)Clasificacion “B15”: Contenido para mayores de 15 años.
            4)Clasificacion “C”: Contenido no apto para menores de 18 años.
            5)Clasificacion “D”: Contenido extremo y exclusivo para adultos.
            --->'''))

            if sel_clasificacion == 1:
                clasificacion="A"
            
            elif sel_clasificacion == 2:
                clasificacion="B"

            elif sel_clasificacion == 3:
                clasificacion="B15"

            elif sel_clasificacion == 4:
                clasificacion="C"
            
            elif sel_clasificacion == 5:
                clasificacion="D"

            precio=int(input("Ingrese el precio del videojuego: "))
            ventas=int(input("Ingrese el numero de ventas del videojuego:"))
            codigo=input("Ingrese el codigo de barra del videojuego:")

            videojuegos = Videojuegos(nombre, categoria, clasificacion, precio, ventas,codigo)


            def getDetails():
                return (videojuegos.nombre, videojuegos.categoria, videojuegos.clasificacion, str(videojuegos.precio), str(videojuegos.ventas), str(videojuegos.codigo_de_barra))
            
            lista_videojuegos.append(getDetails())
    except ValueError:
        print("OPCION INVALIDA, INTENTE DE NUEVO")




#Funcion para crear csv
def crear_csv():
    with open("videojuegos.csv", "w") as videojuegos_csv:
        writer = csv.writer(videojuegos_csv)
        writer.writerow(['NOMBRE', 'CATEGORIA', 'CLASIFICACION', 'PRECIO', 'VENTAS', 'CODIGO'])
        for i in lista_videojuegos:
            writer.writerow(i)


#Funcion para leer csv
def leer_csv():
    with open("videojuegos.csv", "r") as videojuegos_csv:
        for lines in videojuegos_csv:
            print('')
            print(lines)



#Funcion para mostrar videojuegos en el sistema
def mostrar_lista_de_videojuegos():
    print("")
    print("--------------------")
    print("LISTA DE VIDEOJUEGOS")
    print("--------------------")
    print("")

    d=lista_videojuegos
    df= pd.DataFrame(d,columns=['NOMBRE', 'CATEGORIA', 'CLASIFICACION', 'PRECIO', 'VENTAS', 'CODIGO'])
    print(df)


#Funcion para eliminar videojuegos en el sistema
def eliminar_videojuegos():
    try:
        borrar = str(input("Ingrese el codigo del videojuego que desea eliminar:"))
        for i in lista_videojuegos:
            if borrar in i:
                lista_videojuegos.remove(i)
                print("-----------------")
                print("LISTA ACTUALIZADA")
                print("-----------------")
                print("")    
            
            elif borrar not in lista_videojuegos:
                print("NO SE HA ENCONTRADO NINGUN VIDEOJUEGO REGISTRADO CON ESTE CODIGO")
    except ValueError:
        print("VALOR INVALIDO")

    while True:
        try:
            menu_eliminar=int(input('''ESCRIBA QUE DESEA HACER A CONTINUACION:
            1)VER LISTA DE VIDEOJUEGOS ACTUALIZADA
            2)SALIR DE ESTA SECCION
            --->'''))

            if menu_eliminar == 1:
                mostrar_lista_de_videojuegos()
                print("")
            
            elif menu_eliminar == 2:
                print("Saliendo...")
                break
        except ValueError:
            print("VALOR INVALIDO")
            print('')


#Menu para interactuar con las funciones anteriores
def MenuVideojuegos():
    while True:
        try:
            Menu_Videojuegos=int(input('''Ingrese el numero de la accion que desea realizar a continuacion:
            1)Registrar videojuegos
            2)Crear CSV
            3)Leer CSV
            4)Mostrar videojuegos registrados en el sistema
            5)Eliminar un videojuego
            6)Salir al menu principal
            ---->'''))


            if Menu_Videojuegos == 1:
                print('')
                registrar()
                continue

            elif Menu_Videojuegos == 2:
                print("")
                crear_csv()
                print("ARCHIVO CSV CREADO CON EXITO!")
                print("")
                continue

            elif Menu_Videojuegos == 3:
                print('')
                leer_csv()
                continue

            elif Menu_Videojuegos == 4:
                print('')
                mostrar_lista_de_videojuegos()
                continue

            elif Menu_Videojuegos == 5:
                print("")
                eliminar_videojuegos()
                continue

            elif Menu_Videojuegos == 6:
                print('')
                break                

            else:
                print("OPCION INVALIDA, INTENTE DE NUEVO")
                continue

        except ValueError:
            print('SOLO SE PERMITEN NUMEROS, POR FAVOR INTENTE DE NUEVO')
