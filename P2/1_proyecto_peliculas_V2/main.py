'''
Crear un proyecto que permita administrar peliculas
Colocar un menu de opciones par agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas
Nota 1: Utilizar funciones y mandar a llamar desde otro archivo (modulo)
Nota 2: Utilizar diccionarios para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas

'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print(F"\n\t\t\t.:::Gestion de Peliculas::.\n\n\t1.-Crear\n\t2.-Borrar\n\t3.-Mostrar\n\t4.-Agregar Caracteristica\n\t5.-Modificar Carcateristica\n\t6.-Borrar caracteristica\n\t7.-Salir")
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
            peliculas.agregarCaractPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarCaractPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.borrarCaractPeliculas()
            peliculas.espereTecla()
        case "7":
            opcion=False
            print(F"\n\tTerminaste la ejecucion del Sistema... Gracias")
        case _ : 
            opcion=True
            peliculas.espereTecla()
            print("\n\tOpcion invalida vuelva a intentarlo")
