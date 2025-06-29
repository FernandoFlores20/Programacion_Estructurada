'''
Crear un proyecto que permita administrar peliculas
Colocar un menu de opciones par agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas
Nota 1: Utilizar funciones y mandar a llamar desde otro archivo (modulo)
Nota 2: Utilizar listas para almacenar los nombres de peliculas

'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print(F"\n\t\t\t.:::Gestion de Peliculas::.\n\n\t1.-Agregar\n\t2.-Borrar\n\t3.-Modificar\n\t4.-Mostrar\n\t5.-Buscar\n\t6.-Limpiar\n\t7.-Salir")
    opcion=input(f"\t\tElige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modifcarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            opcion=False
            print(F"\n\tTerminaste la ejecucion del Sistema... Gracias")
        case _ : 
            opcion=True
            peliculas.espereTecla()
            print("\n\tOpcion invalida vuelva a intentarlo")
