"""Reglas de validacion de los posts."""

CLAVES_REQUERIDAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post, estados_validos):
    """
    Verifica las reglas de negocio de un post.
    Retorna True si es valido, o un string con todos los errores encontrados.
    """
    if not isinstance(post, dict):
        return "Post invalido: no es un diccionario."

    errores = []

    # 1) Claves requeridas (con 'in', para no lanzar KeyError)
    for clave in CLAVES_REQUERIDAS:
        if clave not in post:
            errores.append(f"falta la clave '{clave}'")

    # 2) Titulo y contenido no vacios
    if "titulo" in post and not str(post["titulo"]).strip():
        errores.append("el titulo esta vacio")
    if "contenido" in post and not str(post["contenido"]).strip():
        errores.append("el contenido esta vacio")

    # 3) Autor: diccionario con nombre
    if "autor" in post:
        autor = post["autor"]
        if not isinstance(autor, dict):
            errores.append("el autor no es un diccionario")
        elif not str(autor.get("nombre", "")).strip():
            errores.append("el autor no tiene nombre")

    # 4) Tags guardados como lista
    if "tags" in post:
        if not isinstance(post["tags"], list):
            errores.append("los tags no estan guardados como lista")
        elif not post["tags"]:
            errores.append("no tiene tags cargados")

    # 5) Estado valido
    if "estado" in post and post["estado"] not in estados_validos:
        errores.append(f"el estado '{post['estado']}' no es valido")

    if errores:
        return f"Post invalido (id {post.get('id', '?')}): {', '.join(errores)}."
    return True


def validar_todos_los_posts(lista, estados_validos):
    """Valida cada post, muestra el resultado y retorna una lista de (id, resultado)."""
    print("\n=== VALIDACION DE POSTS ===")
    if not lista:
        print("No hay posts cargados.")
        return []

    resultados = []
    for post in lista:
        resultado = validar_post(post, estados_validos)
        id_post = post.get("id", "?") if isinstance(post, dict) else "?"
        resultados.append((id_post, resultado))
        if resultado is True:
            print(f"  Post {id_post}: OK")
        else:
            print(f"  Post {id_post}: {resultado}")
    return resultados
