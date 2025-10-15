from libro import Libro, LibroDigital
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                return True
        return False

    def marcar_como_prestado(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro is None:
            raise ValueError("Libro no encontrado")
        libro.libro_prestado()

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro is None:
            raise ValueError("Libro no encontrado")
        libro.devolver()

    def cargar_libros_desde_archivo(self, nombre_archivo='biblioteca.txt'):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    partes = linea.split('|')
                    if len(partes) == 4:
                        titulo, autor, ano_publicacion, formato = partes
                        if formato:
                            libro = LibroDigital(titulo, autor, int(ano_publicacion), formato)
                        else:
                            libro = Libro(titulo, autor, int(ano_publicacion))
                        self.agregar_libro(libro)
                    else:
                        print(f"Formato de línea inválido: {linea}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")

    def guardar_libros_en_archivo(self, nombre_archivo='biblioteca.txt'):
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for libro in self.libros:
                    archivo.write(str(libro) + '\n')
            print(f"Libros guardados en el archivo {nombre_archivo}.")
        except Exception as e:
            print(f"Error al guardar libros en el archivo {nombre_archivo}: {e}")
 