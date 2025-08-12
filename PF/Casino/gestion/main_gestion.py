def mostrar_menu_gestion():
    import gestion.gestion

    GOLD = "\033[38;5;220m"
    BLACK = "\033[30m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    opcion1=True
    opcion2=True
    while opcion1:
        gestion.gestion.borrarPantalla()
        print(f"{BLACK}{GOLD}{BOLD}\n\t\t╔{'═'*38}╗")
        print(f"\t\t║{' ' * 38}║")
        print(f"\t\t║{WHITE}{GOLD}{BOLD}{':::. Gestión del casino .:::'.center(38)}{RESET}{GOLD}{BOLD}║")
        print(f"\t\t║{' ' * 38}║")
        print(f"\t\t╚{'═'*38}╝{RESET}")
        print(f"\n{WHITE}{BOLD}\t1. Gestionar clientes")
        print(f"\t2. Gestionar juegos")
        print(f"\t3. Salir{RESET}")
        opcion1=input(f"\n{WHITE}{BOLD}\tElige una opción: {RESET}").upper().strip()
        match opcion1:
            case "1":
                opcion2=True
                while opcion2:
                    gestion.gestion.borrarPantalla()
                    print(f"{BLACK}{GOLD}{BOLD}\n\t\t╔{'═'*38}╗")
                    print(f"\t\t║{' ' * 38}║")
                    print(f"\t\t║{WHITE}{GOLD}{BOLD}{':::. Gestión de clientes .:::'.center(38)}{RESET}{GOLD}{BOLD}║")
                    print(f"\t\t║{' ' * 38}║")
                    print(f"\t\t╚{'═'*38}╝{RESET}")
                    print(f"\n{WHITE}{BOLD}\t1. Crear cliente")
                    print(f"\t2. Borrar cliente")
                    print(f"\t3. Mostrar cliente")
                    print(f"\t4. Buscar cliente")
                    print(f"\t5. Modificar cliente")
                    print(f"\t6. Exportar a Excel")
                    print(f"\t7. Salir{RESET}")
                    opcion2=input(f"\n{WHITE}{BOLD}\tElige una opción: {RESET}").upper().strip()
                    match opcion2:
                        case "1":
                            gestion.gestion.crearCliente()
                            gestion.gestion.espereTecla()
                        case "2":
                            gestion.gestion.borrarCliente()
                            gestion.gestion.espereTecla()
                        case "3":
                            gestion.gestion.mostrarCliente()
                            gestion.gestion.espereTecla()
                        case "4":
                            gestion.gestion.buscarCliente()
                            gestion.gestion.espereTecla()
                        case "5":
                            gestion.gestion.modificarCliente()
                            gestion.gestion.espereTecla()
                        case "6":
                            gestion.gestion.exportarClientesExcel()
                            gestion.gestion.espereTecla()
                        case "7":
                            opcion2=False
                            print(f"\n{GOLD}{BOLD}\t\u1F6AA Terminaste la ejecución del Sistema... Gracias{RESET}")
                        case _ : 
                            print(f"\n{GOLD}{BOLD}\tOpción inválida, vuelva a intentarlo{RESET}")
            case "2":
                opcion2=True
                while opcion2:
                    gestion.gestion.borrarPantalla()
                    print(f"{BLACK}{GOLD}{BOLD}\n\t\t╔{'═'*38}╗")
                    print(f"\t\t║{' ' * 38}║")
                    print(f"\t\t║{WHITE}{GOLD}{BOLD}{':::. Gestión de juegos .:::'.center(38)}{RESET}{GOLD}{BOLD}║")
                    print(f"\t\t║{' ' * 38}║")
                    print(f"\t\t╚{'═'*38}╝{RESET}")
                    print(f"\n{WHITE}{BOLD}\t1. Crear juego")
                    print(f"\t2. Borrar juego")
                    print(f"\t3. Mostrar juego")
                    print(f"\t4. Buscar juego")
                    print(f"\t5. Modificar juego")
                    print(f"\t6. Exportar a Excel")
                    print(f"\t7. Salir{RESET}")
                    opcion2=input(f"\n{WHITE}{BOLD}\tElige una opción: {RESET}").upper().strip()
                    match opcion2:
                        case "1":
                            gestion.gestion.crearJuego()
                            gestion.gestion.espereTecla()
                        case "2":
                            gestion.gestion.borrarJuego()
                            gestion.gestion.espereTecla()
                        case "3":
                            gestion.gestion.mostrarJuego()
                            gestion.gestion.espereTecla()
                        case "4":
                            gestion.gestion.buscarJuego()
                            gestion.gestion.espereTecla()
                        case "5":
                            gestion.gestion.modificarJuego()
                            gestion.gestion.espereTecla()
                        case "6":
                            gestion.gestion.exportarJuegosExcel()
                            gestion.gestion.espereTecla()
                        case "7":
                            opcion2=False
                            print(f"\n{GOLD}{BOLD}\t\u1F6AA Terminaste la ejecución del Sistema... Gracias{RESET}")
                        case _ : 
                            print(f"\n{GOLD}{BOLD}\tOpción inválida, vuelva a intentarlo{RESET}")
            case "3":
                gestion.gestion.borrarPantalla()
                opcion1=False