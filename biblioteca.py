from libro import Libro, LibroDigital
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
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

    def cargar_libros_desde_archivo(self, nombre_archivo):
        import json
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            for item in datos:
                if 'formato' in item:
                    libro = LibroDigital(item['titulo'], item['autor'], item['ano_publicacion'], item['formato'])
                else:
                    libro = Libro(item['titulo'], item['autor'], item['ano_publicacion'])
                libro.disponible = item.get('disponible', True)
                self.agregar_libro(libro)

    def guardar_libros_en_archivo(self, nombre_archivo='biblioteca.txt'):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea.strip())
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")

    def guardar_en_archivo(self, nombre_archivo='biblioteca.txt'):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for libro in self.libros:
                archivo.write(str(libro) + '\n')
