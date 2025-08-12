import gestion.gestion
import juegos
import globales
import getpass
import hashlib
import juegos.main_juegos
import gestion.main_gestion

GOLD = "\033[38;5;220m"
BLACK = "\033[30m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def banner():
    print(f"{BLACK}{GOLD}{BOLD}")
    print(f"{BOLD}╔{'═' * 46}╗")
    print(f"{BOLD}║{' ' * 46}║")
    print(f"║{WHITE}{GOLD}{BOLD}{'🎰  PAIR OF AS  🎰'.center(44)}{RESET}{GOLD}{BOLD}║")
    print(f"{BOLD}║{' ' * 46}║")
    print(f"{BOLD}╚{'═' * 46}╝{RESET}")

def menu():
    print(f"{WHITE}{BOLD}\nSeleccione una opción:")
    print(f"{GOLD}{BOLD}  1.{WHITE}{BOLD} Iniciar sesión")
    print(f"{GOLD}{BOLD}  2.{WHITE}{BOLD} Crear cuenta")
    print(f"{GOLD}{BOLD}  3.{WHITE}{BOLD} Salir{RESET}")

def hash_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

banner()
while True:
    gestion.gestion.borrarPantalla()
    banner()
    menu()
    opc = input(f"{BOLD}").strip()
    match opc:
        case "1":
            gestion.gestion.borrarPantalla()
            banner()
            cancelar = input(f"{WHITE}{BOLD}Si no quieres iniciar sesión pulsa <Enter> para cancelar, pulsa cualquier otra tecla para continuar: {RESET}{BOLD}").upper().strip()
            if cancelar == "":
                print(f"\n{GOLD}{BOLD}Has cancelado la operación de inicio de sesión.{RESET}")
                gestion.gestion.espereTecla()
                continue
            while True:
                gestion.gestion.borrarPantalla()
                banner()
                telefono = input(f"{WHITE}{BOLD}Por favor ingrese su número de teléfono (10 dígitos): {RESET}{BOLD}")
                if telefono.isdigit() and len(telefono) == 10:
                    break
                print(f"{GOLD}{BOLD}Número inválido. Intente de nuevo.{RESET}")
            contraseña = hash_contraseña(getpass.getpass(f"{WHITE}{BOLD}Por favor ingrese su contraseña: {RESET}{BOLD}"))
            if telefono == "6181696301" and contraseña == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3":
                print(f"\n{GOLD}{BOLD}¡Acceso exitoso! Bienvenido al apartado de gestión.{RESET}")
                gestion.gestion.espereTecla()
                gestion.main_gestion.mostrar_menu_gestion()
            else:
                exito, dinero, id_cliente = gestion.gestion.iniciarSesion(telefono, contraseña)
                if exito:
                    globales.dinero_cliente = dinero
                    globales.telefono_cliente = telefono
                    globales.id_cliente = id_cliente
                    print(f"\n{GOLD}{BOLD}¡Acceso exitoso! Bienvenido al apartado de juegos.{RESET}")
                    gestion.gestion.espereTecla()
                    juegos.main_juegos.mostrar_menu_juegos()
                    gestion.gestion.borrarPantalla()
                    gestion.gestion.actualizarDinero()
                    gestion.gestion.actualizarId()
                else:
                    print(f"\n{GOLD}{BOLD}Teléfono o contraseña incorrectos.{RESET}")
                    gestion.gestion.espereTecla()
        case "2":
            gestion.gestion.borrarPantalla()
            banner()
            gestion.gestion.crearCliente()
        case "3":
            gestion.gestion.borrarPantalla()
            print(f"\n{GOLD}{BOLD}Gracias por usar el sistema del casino, hasta luego.{RESET}\n")
            break
        case _:
            print(f"\n{GOLD}{BOLD}Por favor ingrese una opción válida.{RESET}")