from controller.FileController import FileController


class LibroController:
    def __init__(self):
        self.libros = []
        self.file_controller = FileController()

    # Método para agregar libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para mostrar los libros, recorriendo el array llamando a cada método de cada libro para mostrar su información e imprimirla
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.informacion_libro())

    # Método para eliminar libro, pasándole el ID del libro
    def eliminar_libro(self, id_libro):
        self.libros = [libro for libro in self.libros if libro.id != id_libro]

    # Método para editar el libro, se le pasa el ID del libro que va a editar y la nueva información
    def editar_libro(self, id_libro, nuevo_titulo, nuevo_autor, nuevo_anio_publicacion):
        # Comprueba que existe el libro con el ID que le has pasado
        for libro in self.libros:
            if libro.id == id_libro:
                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                libro.anio_publicacion = nuevo_anio_publicacion
                break
