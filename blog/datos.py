"""Estructuras de datos base del blog."""

perfil_autor = {
    "nombre": "Romina Vogeli",
    "bio": "Analisis de datos y machine learning.",
    "especialidad": "Data Science",
    "redes_sociales": ["@romivogeli", "@romina_ml"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"analisis_de_datos", "machine_learning", "python", "sql",
                  "power_bi", "tableau", "excel"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Instalacion de Python y primer script.",
        "autor": perfil_autor,
        "tags": ["python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Analizando datos con pandas",
        "contenido": "Como cargar y explorar un DataFrame.",
        "autor": perfil_autor,
        "tags": ["python", "pandas", "DataFrames"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Uso de diccionarios anidados en Python.",
        "autor": perfil_autor,
        "tags": ["python", "Diccionarios"],
        "estado": "archivado"
    },
    {
        # Post incompleto a proposito, para probar validar_post():
        # falta la clave "autor", titulo y contenido vacios,
        # tags no es una lista y "revision" no es un estado valido.
        "id": 4,
        "titulo": "",
        "contenido": "",
        "tags": "python",
        "estado": "revision"
    }
]
