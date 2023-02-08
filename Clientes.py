
#Se importan csv y pandas para el manejo de archivos csv
import csv
import pandas as pd

#Se crea una lista que guarda los datos de los clientes
listaclientes=[]

#Se crea la clase clientes con nombre, email, telefono y cedula como atributos. 
class Clientes:
    def __init__(self,name,email,phone,cedula):
        self.name = name
        self.email = email
        self.phone = phone
        self.cedula = cedula

#Se crea la funcion que va a registrar los datos de los clientes.
def registrar():
    print('')
    try:
        x=int(input("Indique la cantidad de clientes que desea registrar: "))


        for i in range(0,x):
        

            nombre = str(input("Ingrese el nombre del cliente:"))
            email=input("Ingrese la direccion de correo del cliente: ")
            numero=str(input("Ingrese el numero de telefono del cliente: "))
            cedula=int(input("Ingrese la cedula del cliente (sin guiones): "))

            clientes = Clientes(nombre, email, numero, cedula)


            def getDetails():
                return (clientes.name, clientes.email, str(clientes.phone), str(clientes.cedula))
            
            listaclientes.append(getDetails())

    except ValueError:
        print("OPCION INVALIDA, INTENTE DE NUEVO")

#Se crea la funcion que crea el csv con los datos capturados anteriormente
def crear_csv():
    with open("clientes.csv", "w") as clientes_csv:
        writer = csv.writer(clientes_csv)
        writer.writerow(["Nombre","Email","Numero de telefono","Cedula"])
        for i in listaclientes:
            writer.writerow(i)

#Se crea la funcion que lee el csv ya exportado
def leer_csv():
    with open("clientes.csv", "r") as clientes_csv:
        for lines in clientes_csv:
            print('')
            print(lines)

#Se crea la funcion que muestra los clientes registrados en el sistema.
def mostrar_lista_de_clientes():
    print("")
    print("-----------------")
    print("LISTA DE CLIENTES")
    print("-----------------")
    print("")

    d=listaclientes
    df= pd.DataFrame(d,columns=["Nombre","Email","Numero de telefono","Cedula"])
    print(df)

#La siguiente funcion eliminar un cliente seleccionado por el usuario
def eliminar_clientes():
    try:
        borrar = str(input("Ingrese el numero de cedula del cliente que desea eliminar:"))
        for i in listaclientes:
            if borrar in i:
                listaclientes.remove(i)
                print("-----------------")
                print("LISTA ACTUALIZADA")
                print("-----------------")
                print("")    
            
            elif borrar not in listaclientes:
                print("NO SE HA ENCONTRADO NINGUN CLIENTE REGISTRADO CON ESTE NUMERO DE CEDULA")
    except ValueError:
        print("VALOR INVALIDO")


    while True:
        try:
            menu_eliminar=int(input('''ESCRIBA QUE DESEA HACER A CONTINUACION:
            1)VER LISTA DE CLIENTES ACTUALIZADA
            2)SALIR DE ESTA SECCION
            --->'''))

            if menu_eliminar == 1:
                mostrar_lista_de_clientes()
                print("")
            
            elif menu_eliminar == 2:
                print("Saliendo...")
                break
        except ValueError:
            print("VALOR INVALIDO")
            print('')

#Se crea la funcion que va a contener el menu con todas las funciones anteriores.
def MenuClientes():
    while True:
        try:
            Menu_Clientes=int(input('''Ingrese el numero de la accion que desea realizar a continuacion:
            1)Registrar cliente
            2)Crear CSV
            3)Leer CSV
            4)Mostrar clientes registrados en el sistema
            5)Eliminar un cliente
            6)Salir al menu principal
            ---->'''))


            if Menu_Clientes == 1:
                print('')
                registrar()
                continue

            elif Menu_Clientes == 2:
                print("")
                crear_csv()
                print("ARCHIVO CSV CREADO CON EXITO!")
                print("")
                continue

            elif Menu_Clientes == 3:
                print('')
                leer_csv()
                continue

            elif Menu_Clientes == 4:
                print('')
                mostrar_lista_de_clientes()
                continue

            elif Menu_Clientes == 5:
                print("")
                eliminar_clientes()
                continue

            elif Menu_Clientes == 6:
                print('')
                break                

            else:
                print("OPCION INVALIDA, INTENTE DE NUEVO")
                continue

        except ValueError:
            print('SOLO SE PERMITEN NUMEROS, POR FAVOR INTENTE DE NUEVO')