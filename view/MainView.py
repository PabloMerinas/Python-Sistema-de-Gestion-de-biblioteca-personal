from controller.FileController import FileController
from controller.LibroController import LibroController
from model.Libro import Libro


class MainView:

    def __init__(self):
        # Iniciamos el controlador para poder trabajar con él
        self.libroController = LibroController()
        self.fileController = FileController()

    # Mostramos el menú principal
    def mostrar_menu(self):
        # Pondre que al iniciar el programa lea el archivo y asi recupera los libros
        self.libroController.libros = self.fileController.leer_libros("librosSaved.txt")

        if len(self.libroController.libros) == 0:
            print("Bienvenido! No se ha cargado ningun archivo de libros")
        else:
            print("Bienvenido! Se ha recuperado el ultimo archivo de libros")

        while True:
            print("Menú CRUD:")
            print("1. Crear libro")
            print("2. Eliminar libro")
            print("3. Editar libro")
            print("4. Mostrar todos los libros")
            print("5. Guardar libros")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.eliminar_libro()
            elif opcion == "3":
                self.editar_libro()
            elif opcion == "4":
                self.mostrar_libros()
            elif opcion == "5":
                self.guardar_libros()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    # Mostramos el menú para agregar un libro, pedirá los datos y llamará al método del controlador
    def agregar_libro(self):
        titulo = input("Indica el título del libro: ")
        autor = input("Indica el autor del libro: ")
        anio_publicacion = input("Indica el año de la publicación del libro: ")
        id = input("Indica el ID del libro: ")

        self.libroController.agregar_libro(Libro(titulo=titulo, autor=autor, anio_publicacion=anio_publicacion, id=id))

    # Mostramos el menú para eliminar un libro a través de su ID
    def eliminar_libro(self):
        # Comprobamos que haya libros, en caso de que no avisará que no hay
        if len(self.libroController.libros) != 0:
            print("Lista de libros:")
            self.libroController.mostrar_libros()
            id_libro = input("Indica el ID del libro que quieres eliminar: ")
            self.libroController.eliminar_libro(id_libro)
            print("Libro eliminado correctamente")
        else:
            print("No hay libros")

    # Menú para editar libro, dependiendo del ID
    def editar_libro(self):
        if len(self.libroController.libros) != 0:
            print("Lista de libros:")
            self.libroController.mostrar_libros()
            id_libro = input("Indica el ID del libro que quieres modificar: ")
            # Pedimos los datos nuevos
            nuevo_titulo = input("Introduce el nuevo título: ")
            nuevo_autor = input("Introduce el nuevo autor: ")
            nuevo_anio_publicacion = input("Introduce el nuevo año de publicación: ")

            self.libroController.editar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio_publicacion)
            print("Libro modificado correctamente")
        else:
            print("No hay libros")

    # Muestra los libros del array del controlador
    def mostrar_libros(self):
        self.libroController.mostrar_libros()

    # Opción del menú para guardar los libros
    def guardar_libros(self):
        if len(self.libroController.libros) == 0:
            print("No hay libros para guardar")
        else:
            self.fileController.guardar_libros(self.libroController.libros, "librosSaved.txt")
            print("Libros guardados")


# Ejemplo de uso
if __name__ == "__main__":
    main_view = MainView()
    main_view.mostrar_menu()
