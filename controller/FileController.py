import os
import pickle

class FileController:
    SAVE_FOLDER = "saves"

    @staticmethod
    def guardar_libros(libros, nombre_archivo):
        carpeta_guardado = FileController.SAVE_FOLDER
        ruta_completa = os.path.join(carpeta_guardado, nombre_archivo)

        with open(ruta_completa, 'wb') as file:
            pickle.dump(libros, file)



    @staticmethod
    def leer_libros(nombre_archivo):
        carpeta_guardado = FileController.SAVE_FOLDER
        ruta_completa = os.path.join(carpeta_guardado, nombre_archivo)

        try:
            with open(ruta_completa, 'rb') as file:
                libros = pickle.load(file)
            return libros
        except FileNotFoundError:
            return []
