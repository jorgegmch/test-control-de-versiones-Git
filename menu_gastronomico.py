import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("Presione ENTER para continuar...")

def mensaje_salir():
    print("Gracias por usar el programa.")

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

def cocina_italaiana():
    print("COCINA ITALIANA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_ita = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_ita} ¡Oh ese plato también nos encanta!")

def cocina_mexicana():
    print("COCINA MEXICANA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_mex = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_mex} ¡Oh ese plato también nos encanta!")

def cocina_japonesa():
    print("COCINA JAPONESA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_mex = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_mex} ¡Oh ese plato también nos encanta!")

def cocina_india():
    print("COCINA INDIA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_ind = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_ind} ¡Oh ese plato también nos encanta!")

def cocina_china():
    print("COCINA CHINA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_ch = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_ch} ¡Oh ese plato también nos encanta!")

def cocina_francesa():
    print("COCINA FRANCESA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_frnc = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_frnc} ¡Oh ese plato también nos encanta!")

def cocina_mediterranea():
    print("COCINA MEDITERRÁNEA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_mdt = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_mdt} ¡Oh ese plato también nos encanta!")

def cocina_vegetariana():
    print("COCINA VEGETARIANA")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Jugo de corozo, fresa o uva")
    comentario_vg = input("Cuentanos que plato te ha gustado más: ")
    print(f"{comentario_vg} ¡Oh ese plato también nos encanta!")   

def carnes():
    print("CARNES")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Vino tinto")
    comentario_carnes = input("Cuentanos que corte de carne te gusta más: ")
    print(f"{comentario_carnes} ¡Oh ese corte también nos encanta!")

def postres():
    print("POSTRES")
    print("-" * 50)
    print("Descripción:" \
    "La cocina italiana es famosa por sus sabores frescos y autenticos," \
    "basados en ingredientes simples como tomate, ajo, aceite de oliva y hierbas.")
    print("Platos platos principales")
    print("Pizza margarita: Masa fina cubierta con tomate, mozzarella, y albahaca.")
    print("Pasta carbonara: Espaguetis en salsa de huevo, queso pecorino, panceta y pimienta.")
    print("Risotto al Funghi: Arroz cremoso con setas.")
    print("Bebidas recomendadas: Café")

isActive = True
while isActive:
    choice = menu_gastronimo()

    match choice:
        case "1":
            pass
            pause()
        case "2":
            pass
            pause()
        case "3":
            pass
            pause()
        case "4":
            pass
            pause()
        case "5":
            pass
            pause()
        case "6":
            pass
            pause()
        case "7":
            pass
            pause()
        case "8":
            pass
            pause()
        case "9":
            pass
            pause()
        case "10":
            pass
            pause()
        case "0":
            mensaje_salir()
            break
        case _:
            print("Opción no válida. Intente nuevamente.")
            pause()