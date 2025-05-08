lista_mascotas = []

def agregar_mascota():
    archivo = open('mascotas\mascotas.txt','r+')
    lista_mascotas = archivo.readlines()
    lista_mascotas = [animal.strip() for animal in lista_mascotas]

    raza = input("Ingrese raza de su mascota: ")
    edad = int(input("Ingrese edad de su mascota: "))
    nombre = input("Ingrese nombre de su mascota: ")
    dueño = input("Ingrese dueño de su mascota: ")
    # tipo = input("Ingrese raza de su mascota: ")

    mascota = [raza,edad,nombre,dueño]
    archivo.write(f"{mascota}{'\n'}")

    archivo.close()