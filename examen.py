
peliculas = {
    'P101': ['Luz de Otoño', 'Drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neon', 'accion', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False ],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Codigo Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficcion', 132, 'B', 'Ingles', False]
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4900, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}
    
def mostrar_menu():
    
    print("========MENU PRINCIPAL==========")
    print("1. Cupos por genero")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")
    print("================================")
   
def leer_opcion():
        try:
            opcion = int(input("Ingrese una opcion del menu: "))

            if (opcion >=1 and opcion <=6):
                return opcion
            else:
                print("Error, seleccione una opcion valida")
            
        except ValueError:
            print("La opcion debe ser un numero entero")


def cupos_genero(genero):
    buscar_genero = input("Ingrese genero a consultar: ")
    

def busqueda_precio(p_min, p_max):
    pass

def buscar_codigo(codigo):
   pass
def actualizar_precio(codigo, nuevo_precio):
    pass


def agregar_pelicula():

    try:
        codigo = input("Ingresar codigo de pelicula: ")
        if (not codigo.strip):
            print("EL codigo no debe contener espacios en blanco")


    except ValueError:
        pass
    
    titulo = input("Ingrese el titulo de la pelicula: ")
    genero = input("Ingrese el genero de la pelicula: ")

    try: 
        clasificacion = input("Ingrese la calificacion de la pelicula (A, B, C): ")
        if (clasificacion != "A", "B", "C"):
            print("La clasificacion debe ser A, B o C")
        else:
            print("")

    except ValueError:
        print("Debe ser sin espacios en blanco")


    idioma = input("Ingrese el idioma de la pelicula: ")
    es_3d = input("Ingrese si la pelicula es 3d (S / N): ")
    precio = int(input("Ingrese el precio de la pelicula: "))
    cupos = int(input("Ingrese la cantidad de cupos para la pelicula: "))
    duracion = int(input("Ingrese la duracion de la pelicula en minuntos: "))

    
def eliminar_pelicula():
    pass


while True:

    mostrar_menu()
    opc = leer_opcion()
    try:
        if(opc == 1):
            cupos_genero()
        elif(opc == 2):
            busqueda_precio()
        elif(opc == 3):
            actualizar_precio()
        elif(opc == 4):
            agregar_pelicula()
        elif(opc == 5):
            eliminar_pelicula()
        elif(opc == 6):
            print("Programa finalizado")
            break
    except ValueError:
        pass 
