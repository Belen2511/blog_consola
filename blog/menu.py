"""Menu e interaccion con el usuario (todo el manejo de input() esta aca)."""


def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")


def obtener_opcion_menu():
    """Muestra el menu y retorna la opcion elegida como int (o None si no es un numero)."""
    mostrar_menu()
    entrada = input("Elegi una opcion (1-5): ").strip()
    try:
        return int(entrada)
    except ValueError:
        return None


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios de mas."""
    return input(mensaje).strip()
