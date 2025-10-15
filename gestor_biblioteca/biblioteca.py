from libro import Libro, LibroDigital
import libro
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. {libro}")
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
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if libro.disponible:
                    libro.disponible = False
                    print(f"El libro '{titulo}' ha sido marcado como prestado.")
                    return
                else:
                    print(f"El libro '{titulo}' ya está prestado.")
                    return
        raise ValueError(f"No se encontró el libro '{titulo}' en la biblioteca.")
    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                if not libro.disponible:
                    libro.disponible = True
                    print(f"El libro '{titulo}' ha sido devuelto exitosamente.")
                    return
                else:
                    print(f"El libro '{libro.titulo}' no está prestado.")
                    return
        raise ValueError(f"No se encontró el libro '{titulo}' en la biblioteca.")
    

    def cargar_libros_desde_archivo(self, nombre_archivo='biblioteca.txt'):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split('|')
                    titulo = partes[0]
                    autor = partes[1]
                    ano = int(partes[2])
                    estado = partes[3].strip() == "disponible"  # True si disponible, False si prestado
                    tipo = partes[4]

                    if tipo == "Digital":
                        formato = partes[5] if len(partes) > 5 else "PDF"
                        libro = LibroDigital(titulo, autor, ano, formato)
                    else:
                        libro = Libro(titulo, autor, ano)

                    libro.disponible = estado
                    self.libros.append(libro)

        except FileNotFoundError:
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los libros: {e}")

    def guardar_libros_en_archivo(self, nombre_archivo='biblioteca.txt'):
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for libro in self.libros:
                    estado = "Disponible" if libro.disponible else "Prestado"

                    if isinstance(libro, LibroDigital):
                        # Libro digital: incluye formato
                        linea = f"{libro.titulo}|{libro.autor}|{libro.ano_publicacion}|{estado}|Digital|{libro.formato}"
                    else:
                        # Libro físico: no tiene formato
                        linea = f"{libro.titulo}|{libro.autor}|{libro.ano_publicacion}|{estado}|Físico"

                    archivo.write(linea + '\n')

            print(f"Libros guardados correctamente en {nombre_archivo}.")

        except IOError:
            print(f"No se pudo guardar en el archivo {nombre_archivo}.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
