import calificaciones

def main():
    datos=[]

    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregarCalif(datos)
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalif(datos)
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularCalif(datos)
                calificaciones.espereTecla()
            case "4":
                opcion=False
                print(F"\n\t\U0001F6AA Terminaste la ejecucion del Sistema... Gracias")
            case _ : 
                opcion=True
                print("\n\t\t\u274COpcion invalida vuelva a intentarlo")
                calificaciones.espereTecla()
if __name__=="__main__":
    main()