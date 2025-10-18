import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("Presione ENTER para continuar...")

def menu_gastronimo():
    clear_screen()
    print("BIENVENIDO A LA GUÍA DE MENÚS GASTRONÓMICOS")
    print("-" * 50)
    print("1. Cocina italiana")
    print("2. Cocina mexicana")
    print("3. Cocina japonesa")
    print("4. Cocina india")
    print("5. Cocina china")
    print("6. Cocina francesa")
    print("7. Cocina mediterránea")
    print("8. Cocina vegetariana")
    print("9. Carnes")
    print("10. Postres")
    print("0. Salir")
    opcion = input("Ingrese una opción (0-10): ")
    return opcion