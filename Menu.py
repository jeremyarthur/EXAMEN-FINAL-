#Jeremy Arthur Martinez Valoy (Matricula:21-1474)
#EXAMEN FINAL 

'''Mediante el uso de Programacion Orientada a Objetos, 
desarrollar un pequeño sistema que permita el mantenimiento de las ventas de videojuegos de PowerGames.'''

#Se importan los menus de los archivos que contienen las clases
from Clientes import MenuClientes
from Ventas import MenuVentas
from Videojuegos import MenuVideojuegos


#Mensaje de bienvenida
print("")
print("--------------------------------------------------")
print("BIENVENIDO AL SISTEMA DE VIDEOJUEGOS DE POWERGAMES")
print("--------------------------------------------------")
print("")

print("--------------------------------------------------")
print("|                     MENU                       |")
print("--------------------------------------------------")
print('')


#Se crea un menu principal dentro de un ciclo (incluyendo control de databasura) para acceder a los 3 archivos.
while True:
    try:

        Menu_Principal= int(input('''INGRESE EL NUMERO DE LA ACCION QUE DESEA REALIZAR
        1)Acceder a "Clientes"
        2)Acceder a "VideoJuegos"
        3)Acceder a "Ventas"
        4)Salir
        ------->'''))

        if Menu_Principal==1:
            print('')
            MenuClientes()
            continue

        elif Menu_Principal==2:
            print('')
            MenuVideojuegos()
            continue

        elif Menu_Principal ==3:
            print('')
            MenuVentas()
            continue

        elif Menu_Principal ==4:
            print('')
            print("GRACIAS POR UTILIZAR EL PROGRAMA")
            break


    except ValueError:
        print('')
        print("----------------------------------------------------")
        print("SOLO SE PERMITEN NUMEROS, POR FAVOR INTENTE DE NUEVO")
        print("----------------------------------------------------")
        print('')
