peliculas=[]
#peli=""

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t... Oprima cualquier tecla pra continuar ...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar peliculas::.\n")
    peliculas.append(input("Ingrese el nombre de la pelicula: ").upper().strip())
    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():
    borrarPantalla()
    if len(peliculas)>0:
        print("\n\t.::Mostrar peliculas::.\n")
        for i in range (0,len(peliculas)):
            #peli=peliculas[i]
            print(f"{i+1}\t{peliculas[i]}")
    else:
        print("\n\t.::No hay peliculas por el momento::.\n")

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Limpiar o borrar todas las peliculas::.")
    resp=input("Deseas borrar todas las peliculas del sistema? (si/no)").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar peliculas::.\n")
    busq=input("Ingrese la pelicula que quiere buscar: ").upper().strip()
    if not (busq in peliculas):
        print("\n\t.::Esta pelicula no existe en el sistema::.\n")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if busq==peliculas[i]:
                print(f"\n\tLa pelicula {busq} se encontro en la posicion {i+1}")
                peliculas.count(busq)
                encontro+=1
    print(f"\nTenemos {encontro} pelicula(s) con este titulo")

def modifcarPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar peliculas::.\n")
    busq=input("Ingrese la pelicula que quiere modificar: ").upper().strip()
    encontro=0
    if not (busq in peliculas):
        print("\n\t.::Esta pelicula no existe en el sistema::.\n")
    else:
        for i in range(0,len(peliculas)):
            if busq==peliculas[i]:
                resp=input("Desea actualizar la pelicula? (si/no)").lower()
                if resp=="si":
                    peliculas[i]=input("\nIntroduce el nuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
    print(f"\n Se modifico {encontro} pelicula(s) con este titulo")
            
def borrarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar peliculas::.\n")
    busq=input("Ingrese la pelicula que quiere borrar: ").upper().strip()
    encontro=0
    if not (busq in peliculas):
        print("\n\t.::Esta pelicula no existe en el sistema::.\n")
    else:
        resp="si"
        while busq in peliculas and resp=="si":
            resp=input("Desea actualizar la pelicula? (si/no)").lower()
            if resp=="si":
                posicion=peliculas.index(busq)
                print(f"\nLa pelicula que se borro es {busq} y estaba en la posicion {posicion+1}")
                peliculas.remove(busq)
                encontro+=1
                print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
        print(f"\n Se borro {encontro} pelicula(s) con este titulo")
