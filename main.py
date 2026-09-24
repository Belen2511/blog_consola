"""Punto de entrada del sistema de blog por consola."""

from blog.datos import posts, estados_post
from blog.menu import obtener_opcion_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos_los_posts


def main():
    while True:
        opcion = obtener_opcion_menu()

        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            termino = pedir_texto("Ingresa el titulo (o parte de el) a buscar: ")
            buscar_por_titulo(posts, termino)
        elif opcion == 3:
            tag = pedir_texto("Ingresa el tag a filtrar: ")
            filtrar_por_tag(posts, tag)
        elif opcion == 4:
            validar_todos_los_posts(posts, estados_post)
        elif opcion == 5:
            print("\nSaliendo del blog. Hasta la proxima!")
            break
        else:
            print("\nOpcion invalida. Por favor elegi un numero del 1 al 5.")


if __name__ == "__main__":
    main()
