
#Se crea una lissta que captura los datos de las ventas
listaventas=[]

#se importan pandas y csv para los datos csv
import csv
import pandas as pd



#se crea la clase ventas
class Ventas:
    def __init__(self,nombre_del_juego, ganancias_ventas, cantidad_ventas):
        self.nombre_del_juego = nombre_del_juego
        self.ganancias_ventas = ganancias_ventas
        self.cantidad_ventas = cantidad_ventas


#Se crea la funcion que va a registrar los datos de las ventas
def registrar():
    print('')
    try:
        x=int(input("Indique la cantidad de ventas que desea registrar: "))


        for i in range(0,x):
        

            nombre = str(input("Ingrese el nombre del juego:"))
            precio= int(input("Ingrese el precio del videojuego:"))
            cantidad= int(input("Ingrese el cantidad vendida"))
            
            gan=precio*cantidad
            ventas = Ventas(nombre,gan,cantidad)


            def getDetails():
                return (ventas.nombre_del_juego, str(ventas.ganancias_ventas), str(ventas.cantidad_ventas))
            
            listaventas.append(getDetails())

    except ValueError:
        print("OPCION INVALIDA, INTENTE DE NUEVO")


#se crea la funcion que va a crear los csv
def crear_csv():
    with open("ventas.csv", "w") as ventas_csv:
        writer = csv.writer(ventas_csv)
        writer.writerow(['NOMBRE DEL JUEGO','GANANCIAS DE VENTAS','CANTIDAD VENDIDA'])
        for i in listaventas:
            writer.writerow(i)


#Se crea la funcion que va a leer el csv ya exportado
def leer_csv():
    with open("ventas.csv", "r") as ventas_csv:
        for lines in ventas_csv:
            print('')
            print(lines)

#Se crea la funcion que va a mostrar las ventas del sistema
def mostrar_lista_de_ventas():
    print("")
    print("---------------")
    print("LISTA DE VENTAS")
    print("---------------")
    print("")

    d=listaventas
    df= pd.DataFrame(d,columns=['NOMBRE DEL JUEGO','GANANCIAS DE VENTAS','CANTIDAD VENDIDA'])
    print(df)


#Se crea la funcion que va eliminar ventas seleccionadas
def eliminar_venta():
    try:
        borrar = str(input("Ingrese el nombre del juego cuya venta desea eliminar:"))
        for i in listaventas:
            if borrar in i:
                listaventas.remove(i)
                print("-----------------")
                print("LISTA ACTUALIZADA")
                print("-----------------")
                print("")    
            
            elif borrar not in listaventas:
                print("NO SE HA ENCONTRADO NINGUN JUEGO REGISTRADO CON ESTE NOMBRE")
    except ValueError:
        print("VALOR INVALIDO")

    while True:
        try:
            menu_eliminar=int(input('''ESCRIBA QUE DESEA HACER A CONTINUACION:
            1)VER LISTA DE VENTAS ACTUALIZADA
            2)SALIR DE ESTA SECCION
            --->'''))

            if menu_eliminar == 1:
                mostrar_lista_de_ventas()
                print("")
            
            elif menu_eliminar == 2:
                print("Saliendo...")
                break
        except ValueError:
            print("VALOR INVALIDO")
            print('')

#Se crea el menu para interactuar con todas las funciones anteriores
def MenuVentas():
    while True:
        try:
            Menu_Ventas=int(input('''Ingrese el numero de la accion que desea realizar a continuacion:
            1)Registrar venta
            2)Crear CSV
            3)Leer CSV
            4)Mostrar ventas registradas en el sistema
            5)Eliminar una venta
            6)Salir al menu principal
            ---->'''))


            if Menu_Ventas == 1:
                print('')
                registrar()
                continue

            elif Menu_Ventas == 2:
                print("")
                crear_csv()
                print("ARCHIVO CSV CREADO CON EXITO!")
                print("")
                continue

            elif Menu_Ventas == 3:
                print('')
                leer_csv()
                continue

            elif Menu_Ventas == 4:
                print('')
                mostrar_lista_de_ventas()
                continue

            elif Menu_Ventas == 5:
                print("")
                eliminar_venta()
                continue

            elif Menu_Ventas == 6:
                print('')
                break                

            else:
                print("OPCION INVALIDA, INTENTE DE NUEVO")
                continue

        except ValueError:
            print('SOLO SE PERMITEN NUMEROS, POR FAVOR INTENTE DE NUEVO')