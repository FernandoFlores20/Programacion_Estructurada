'''
Dict u objeto que permita almacenar los siguientes atributos: nombre, categoria, clasificacion, genero, idioma de peliculas
'''
'''
pelicula=(
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "idioma":""
    )
'''
pelicula={}
#peli=""

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input(f"\n\t... Oprima cualquier tecla pra continuar ...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar peliculas::.\n")
    '''
    atributo=input("Ingresa la caracteristica: ").upper().strip()
    valor_atributo=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelicula.update(atributo,valor_atributo)
    '''
    resp="si"
    while resp=="si":
        pelicula.update({"nombre":input("Ingrese el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("Ingrese la categoria: ").upper().strip()})
        pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper().strip()})
        pelicula.update({"genero":input("Ingrese el genero: ").upper().strip()})
        pelicula.update({"idioma":input("Ingrese el idioma: ").upper().strip()})
        resp=input("Quiere agregar mas cosas?").lower
    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.::Mostrar caracteristicas::.\n")
    if (len(pelicula)>0):
        for i in pelicula:
            print(f"{i}:  {pelicula[i]}")
    else:
        print("\n\t.::No hay atributos por el momento::.\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar o quitar la pelicula::.\n")
    if len(pelicula)>0:
        resp=input("Desea borrar todas las caracteristicas?(si/no): ").lower().strip()
        if resp=="si":
            pelicula.clear()
    else:
        print("No hay peliculas que borrar ")
    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
   
def agregarCaractPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar un atributo::.\n")
    atributo=input("Ingresa la caracteristica: ").lower().strip()
    valor_atributo=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelicula.update({atributo: valor_atributo})
    print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")

def modificarCaractPeliculas():
    borrarPantalla()
    print("\n\t .::Modificar una caracteristica::.")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
            resp=input(f"Deseas modificar el valor de la caracteristica {i}?: (si/no)").lower().strip()
            if resp=="si":
                valor=input(f"Ingrese el nuevo valor de la caracteristica {i}: ").upper().strip()
                pelicula.update({i:valor})
                print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
    else:
        print("\n\t .::No hay peliculas::.")
    '''
    borrarPantalla()
    print("\n\t.::Modificar un atributo::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}:  {pelicula[i]}")
            resp=input("Desea modificar el valor de este atributo?: ").lower().strip()
            if resp=="si": 
                atributo_valor=input("Ingrese el nuevo valor: ").upper().strip()
                pelicula[i]=atributo_valor
                print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")
                espereTecla()
            borrarPantalla()
            print("\n\t.::Modificar un atributo::.\n")
    else:
        print("No hay atributos registrados")
    '''

def borrarCaractPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar o quitar una caracteristica::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}:  {pelicula[i]}")
        resp=input("Desea borrar una caracteristica(si/no): ").lower().strip()
        if resp=="si":
            resp2=input("Ingrese la caracteristica que desea borrar: ").lower().strip()
            if resp2 in pelicula:
                pelicula.pop(resp2)
                print("\n\t\t.::LA OPERACION SE REALIZO CON EXITO!::.")      
            else:
                print("No hay una caracteristica llamada asi")        
    else:
         print("No hay valores registrados")

    '''
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

#def limpiarPeliculas():
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
'''