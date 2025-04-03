import os
import time

def menu():
    print("\nBienvenido a la agenda de contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Cargar contactos desde archivo")
    print("7. Guardar contactos en archivo")
    print("8. Salir")

def agregar_contacto():
    print("\nAgregar contacto")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    contacto = {
        "id": len(agenda) + 1,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    agenda.append(contacto)
    print("Contacto agregado")

def ver_contactos():
    print("\nLista de contactos:")
    if not agenda:
        print("No hay contactos guardados.")
    else:
        for contacto in agenda:
            print(f"ID: {contacto['id']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            print("-" * 20)

def buscar_contacto():
    print("\nSeleccione una opción de búsqueda")
    print("1. Nombre")
    print("2. Teléfono")
    print("3. Email")

    opcion = input("Opción: ")
    encontrado = False

    if opcion == "1":
        nombre = input("Nombre: ")
        for contacto in agenda:
            if contacto["nombre"] == nombre:
                encontrado = True
                print_contacto(contacto)
    elif opcion == "2":
        telefono = input("Teléfono: ")
        for contacto in agenda:
            if contacto["telefono"] == telefono:
                encontrado = True
                print_contacto(contacto)
    elif opcion == "3":
        email = input("Email: ")
        for contacto in agenda:
            if contacto["email"] == email:
                encontrado = True
                print_contacto(contacto)
    else:
        print("Opción no válida")
    
    if not encontrado:
        print("Contacto no encontrado")

def print_contacto(contacto):
    print(f"\nID: {contacto['id']}")
    print(f"Nombre: {contacto['nombre']}")
    print(f"Teléfono: {contacto['telefono']}")
    print(f"Email: {contacto['email']}")
    print("-" * 20)

def editar_contacto():
    ver_contactos()
    id = int(input("\nID del contacto a editar: "))
    encontrado = False

    for contacto in agenda:
        if contacto["id"] == id:
            encontrado = True
            print("\n¿Qué deseas editar?")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            opcion = input("Opción: ")

            if opcion == "1":
                contacto["nombre"] = input("Nuevo nombre: ")
            elif opcion == "2":
                contacto["telefono"] = input("Nuevo teléfono: ")
            elif opcion == "3":
                contacto["email"] = input("Nuevo email: ")
            else:
                print("Opción no válida")
            
            print("Contacto editado")
            break
    
    if not encontrado:
        print("Contacto no encontrado")

def eliminar_contacto():
    ver_contactos()
    id = int(input("\nID del contacto a eliminar: "))
    encontrado = False

    for contacto in agenda:
        if contacto["id"] == id:
            encontrado = True
            agenda.remove(contacto)
            print("Contacto eliminado")
            break

    if not encontrado:
        print("Contacto no encontrado")

def cargar_contactos():
    try:
        with open("contactos.csv", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                contacto = linea.strip().split(",")
                agenda.append({
                    "id": len(agenda) + 1,
                    "nombre": contacto[0],
                    "telefono": contacto[1],
                    "email": contacto[2]
                })
        print("Contactos cargados exitosamente")
    except FileNotFoundError:
        print("El archivo no existe")

def guardar_contactos():
    with open("contactos.csv", "w") as archivo:
        for contacto in agenda:
            archivo.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['email']}\n")
    print("Contactos guardados exitosamente")

def limpiar_pantalla():
    input("\nPresiona Enter para continuar...")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    global agenda
    agenda = []
    
    while True:
        menu()
        opcion = input("Opción: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            editar_contacto()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            cargar_contactos()
        elif opcion == "7":
            guardar_contactos()
        elif opcion == "8":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida")
        
        limpiar_pantalla()

if __name__ == "__main__":
    main()