
# Blog por consola (versión modular)

Sistema de blog por consola en Python. Permite listar posts, buscar por título, filtrar por tag y validar la estructura de los posts cargados en memoria.

Esta versión reorganiza el script único del Módulo 4 en un paquete con módulos separados por responsabilidad.

## Cómo ejecutarlo

Requisito: Python 3.8 o superior. No usa librerías externas.

Desde la carpeta raíz del proyecto (`blog_consola/`):

```bash
python main.py
```

El archivo que se ejecuta es **`main.py`**.

## Estructura del proyecto
...

blog_consola/
│
├── main.py              # Punto de entrada: arma el flujo del menú
├── README.md
│
└── blog/                # Paquete del sistema
    ├── __init__.py      # Marca la carpeta como paquete
    ├── datos.py         # Datos base del blog
    ├── menu.py          # Menú y manejo de input()
    ├── operaciones.py   # Listar, buscar y filtrar posts
    └── validaciones.py  # Reglas de validación de posts
```

## Qué hace cada módulo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Importa las piezas del paquete `blog`, muestra el menú en un bucle y llama a la función que corresponde a cada opción. La ejecución arranca dentro de `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca `blog/` como un paquete. |
| `blog/datos.py` | `perfil_autor` (dict), `estados_post` (tupla), `etiquetas_blog` (set) y `posts` (lista de dicts). El autor va como diccionario anidado dentro de cada post. El post con id 4 está incompleto a propósito para probar las validaciones. |
| `blog/menu.py` | `mostrar_menu()`, `obtener_opcion_menu()` (devuelve la opción como `int`, o `None` si no se ingresó un número) y `pedir_texto()`. Todos los `input()` están acá. |
| `blog/operaciones.py` | `mostrar_post()`, `listar_posts(lista)`, `buscar_por_titulo(lista, termino)` y `filtrar_por_tag(lista, tag)`. Reciben los datos por parámetro y devuelven los resultados. Búsqueda y filtro usan `.lower()`, así que no distinguen mayúsculas de minúsculas. |
| `blog/validaciones.py` | `validar_post(post, estados_validos)` devuelve `True` o un mensaje con todos los errores. `validar_todos_los_posts(lista, estados_validos)` valida todos los posts y muestra el resultado de cada uno. |

## Reglas de validación

Un post es válido si:

- es un diccionario;
- tiene las claves `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`;
- el título y el contenido no están vacíos;
- el autor es un diccionario y tiene nombre;
- los tags están guardados como lista y no está vacía;
- el estado es uno de los permitidos: `borrador`, `publicado` o `archivado`.

## Opciones del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

1. **Ver todos los posts**: muestra ID, título, autor, tags y estado de cada post.
2. **Buscar por título**: busca coincidencias totales o parciales, sin distinguir mayúsculas de minúsculas.
3. **Filtrar por tag**: muestra los posts que tienen ese tag, sin distinguir mayúsculas de minúsculas.
4. **Validar posts**: indica qué posts son válidos y qué errores tiene cada uno de los demás.
5. **Salir**: muestra un mensaje de despedida y termina el programa.

Si se ingresa algo que no es un número del 1 al 5, el programa avisa que la opción es inválida y vuelve a mostrar el menú.
=======
# blog_consola
Blog por consola organizado en módulos y paquetes
>>>>>>> c801f0729817ad2f4a06a2d2e034fd9b94b12140
