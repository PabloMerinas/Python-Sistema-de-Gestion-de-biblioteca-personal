class Libro:
    def __init__(self, titulo, autor, anio_publicacion, id):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.id = id

    def informacion_libro(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.anio_publicacion}"
