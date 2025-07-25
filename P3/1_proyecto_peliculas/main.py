'''
Crear un proyecto que permita administrar peliculas
Colocar un menu de opciones par agregar, borrar, modificar, mostrar, buscar peliculas
Nota 1: Utilizar funciones y mandar a llamar desde otro archivo (modulo)
Nota 2: Utilizar diccionarios para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas
Nota 3: Implementar y utilizar una BD relacional en MYSQL

'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print(F"\n\t\t\t.:::Gestion de Peliculas::.\n\n\t1.-Crear\n\t2.-Borrar\n\t3.-Mostrar\n\t4.-Buscar pelicula\n\t5.-Borrar pelicula\n\t6.-Modificar pelicula\n\t7.-Salir")
    opcion=input(f"\t\tElige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.modificarPelicula()
            peliculas.espereTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print(F"\n\tTerminaste la ejecucion del Sistema... Gracias")
        case _ : 
            opcion=True
            peliculas.espereTecla()
            print("\n\tOpcion invalida vuelva a intentarlo")