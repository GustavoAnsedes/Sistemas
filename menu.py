#Primera versión sin comprobar que los datos introducidos son válidos
import os
import subprocess
from os import system
system("clear")

#Opciones del menu
def menu():
    print("1. Limpiar la pantalla")
    print("2. Crear un usuario")
    print("3. Borrar un usuario")
    print("4. Cambiar la contraseña de un usuario")
    print("5. Crear un grupo")
    print("6. Borrar un grupo")
    print("7. Crear un directorio")
    print("8. Borrar un directorio")
    print("9. Mostrar la fecha actual")
    print("10. Salir del menu")

#Limpiar pantalla
def opcion1():
    system("clear")

#Funcion crear usuario
def crear_usuario(nombre, directorio):
    subprocess.run(['sudo', 'useradd', '-m', '-d', directorio, '-s', '/bin/bash', nombre])

#Función pedir datos y crearlo
def opcion2():
    nombre = input("Introduce el nombre del usuario: ")
    directorio = input("Introduce el nombre del directorio (/home/nombre): ")
    crear_usuario(nombre, directorio)
    print("Usuario creado.")

#Borrar usuario y su home. Stderr para ocultar mensaje de not found(user mail spool (/var/mail/user) not found)
def borrar_usuario(nombre_usuario):
    subprocess.run(['sudo', 'userdel', '-r', nombre_usuario], stderr=subprocess.DEVNULL)

#Función pedir usuario para borrar y borrarlo
def opcion3():
    nombre_usuario = input("Introduce el nombre del usario que desees borrar: ")
    borrar_usuario(nombre_usuario)
    print("Usuario borrado")

#Funcion para crear una contraseña para el usuario
def cambiar_contraseña(usuario_contr):
    subprocess.run(['sudo', 'passwd', usuario_contr])

#Función pedir el usuario que quiere cambiar la contraseña y cambiarla
def opcion4():
    usuario_contr = input("Introduce el nombre de usuario al que le quieras cambiar la contraseña: ")
    cambiar_contraseña(usuario_contr)

#Función crear grupo
def crear_grupo(nombre_grupo):
    subprocess.run(['sudo', 'groupadd',nombre_grupo])

#Función pedir nombre del grupo y crearlo
def opcion5():
    nombre_grupo = input("Introduce el nombre del grupo a crear: ")
    crear_grupo(nombre_grupo)
    print("Grupo creado.")

#Funcion borrar grupo
def borrar_grupo(nombre_grupo2):
    subprocess.run(['sudo', 'groupdel', nombre_grupo2])

#Funcion pedir nombre de grupo a borrar y borrarlo
def opcion6():
    nombre_grupo2 = input("Introduce el nombre del grupo que quieras borrar: ")
    borrar_grupo(nombre_grupo2)
    print("Grupo borrado.")

#Funcion crear directorio
def crear_directorio(nombre_directorio):
    subprocess.run(['sudo', 'mkdir', nombre_directorio])

#Funcion pedir nombre directorio a crear y crearlo
def opcion7():
    nombre_directorio = input("Introduce el nombre del directorio que quieras crear: ")
    crear_directorio(nombre_directorio)
    print("Grupo creado.")

#Funcion borrar directorio
def borrar_directorio(nombre_directorio2):
    subprocess.run(['sudo', 'rmdir', nombre_directorio2])

#Funcion pedir nombre de grupo a borrar y borrarlo
def opcion8():
    nombre_directorio2 = input("Introduce el nombre del directorio que quieras borrar: ")
    borrar_directorio(nombre_directorio2)
    print("Directorio borrado.")

#Funcion imprimir fecha actual
def opcion9():
    subprocess.run(['date'])

#Escoger opciones del menu
def menu_opciones():
    for _ in range(50):
        menu()
        choice = input("Escoge una de las siguientes opciones: ")

        if choice == '1':
            opcion1()
        elif choice == '2':
            opcion2()
        elif choice == '3':
            opcion3()
        elif choice == '4':
            opcion4()
        elif choice == '5':
            opcion5()
        elif choice == '6':
            opcion6()
        elif choice == '7':
            opcion7()
        elif choice == '8': 
            opcion8()
        elif choice == '9':
            opcion9()
        elif choice == '10':
            break
        else:
            print("No es una opcion válida")

menu_opciones()