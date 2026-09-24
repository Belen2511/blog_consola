"""Operaciones principales del blog: listar, buscar y filtrar."""


def mostrar_post(post):
    """Imprime un post de forma prolija, sin romper si le faltan datos."""
    autor = post.get("autor")
    nombre_autor = autor.get("nombre", "Desconocido") if isinstance(autor, dict) else "Desconocido"
    tags = post.get("tags")
    tags = tags if isinstance(tags, list) else []

    print(f"  ID: {post.get('id', '?')}")
    print(f"  Titulo: {post.get('titulo') or '(sin titulo)'}")
    print(f"  Autor: {nombre_autor}")
    print(f"  Tags: {', '.join(str(t) for t in tags) if tags else '(sin tags)'}")
    print(f"  Estado: {post.get('estado') or '(sin estado)'}")
    print("  " + "-" * 30)


def listar_posts(lista):
    """Muestra todos los posts de la lista y la retorna."""
    print("\n=== TODOS LOS POSTS ===")
    if not lista:
        print("No hay posts cargados.")
        return []
    for post in lista:
        mostrar_post(post)
    return lista


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo titulo contenga el termino (sin distinguir mayusculas)."""
    termino = termino.strip().lower()
    encontrados = [p for p in lista if termino in str(p.get("titulo", "")).lower()]

    print(f"\n=== RESULTADOS PARA '{termino}' ===")
    if not encontrados:
        print("No se encontraron posts con ese titulo.")
        return encontrados
    for post in encontrados:
        mostrar_post(post)
    return encontrados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tengan el tag indicado (sin distinguir mayusculas)."""
    tag = tag.strip().lower()
    encontrados = []
    for p in lista:
        tags = p.get("tags")
        if isinstance(tags, list) and tag in [str(t).lower() for t in tags]:
            encontrados.append(p)

    print(f"\n=== POSTS CON TAG '{tag}' ===")
    if not encontrados:
        print("No se encontraron posts con ese tag.")
        return encontrados
    for post in encontrados:
        mostrar_post(post)
    return encontrados
