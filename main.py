from mascotas.mascotas import agregar_mascota

def menu():
    print()
    print("Bienvenido a veterinaria Arca de Noe")
    print("1. Agregar mascota")
    print("0. Salir")

while True:
    menu()
    opcion = input("Seleccione su opción (0-1)")
    if opcion == "1":
        agregar_mascota()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("opción inválida... Seleccione nuevamente...")