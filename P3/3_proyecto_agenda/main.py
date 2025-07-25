import agenda

def main():
    contactos={}

    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()
        if opcion=="1":
            agenda.agregarContac(contactos)
            agenda.espereTecla()
        elif opcion=="2":
            agenda.mostrarContac(contactos)
            agenda.espereTecla()
        elif opcion=="3":
            agenda.buscarContac(contactos)
            agenda.espereTecla()
        elif opcion=="4":
            agenda.modificarContac(contactos)
            agenda.espereTecla()
        elif opcion=="5":
            agenda.borrarContac(contactos)
            agenda.espereTecla()
        elif opcion=="6":
            opcion=False
            print(F"\n\t\U0001F6AA Terminaste la ejecucion del Sistema... Gracias")
        else:
            opcion=True
            print("\n\t\t\u274COpcion invalida vuelva a intentarlo")  
            agenda.espereTecla()


'''
        match opcion:
            case "1":
                agenda.agregarContac(contactos)
                agenda.espereTecla()
            case "2":
                agenda.mostrarContac(contactos)
                agenda.espereTecla()
            case "3":
                agenda.buscarContac(contactos)
                agenda.espereTecla()
            case "4":
                opcion=False
                print(F"\n\t\U0001F6AA Terminaste la ejecucion del Sistema... Gracias")
            case _ : 
                opcion=True
                print("\n\t\t\u274COpcion invalida vuelva a intentarlo")
                agenda.espereTecla()
'''
if __name__=="__main__":
    main()