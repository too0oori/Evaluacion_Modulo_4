# sistema de gestión de biblioteca

from libro import Libro, LibroDigital
from biblioteca import Biblioteca
def menu():
    print("\nBienvenido al gestor de biblioteca")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Ver todos los libros")
    print("4. Buscar libro")
    print("5. Marcar libro como prestado")
    print("6. Devolver libro")
    print("7. Salir")

def agregar_libro(biblioteca):
    print("\n--AGREGAR LIBRO--:")
    tipo = input("¿Es un libro digital? (s/n): ").strip().lower()
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano_publicacion = input("Año de publicación: ")
    try:
        ano_publicacion = int(ano_publicacion)
    except ValueError:
        print("Año de publicación debe ser un número.")
        return
    
    if tipo == 's':
        formato = input("Formato (e.g., PDF, EPUB): ")
        libro = LibroDigital(titulo, autor, ano_publicacion, formato)
    else:
        libro = Libro(titulo, autor, ano_publicacion)
    biblioteca.agregar_libro(libro)

    print(f"Libro '{titulo}' agregado correctamente.")

def eliminar_libro(biblioteca):
    print("\n--ELIMINAR LIBRO--:")
    try:
        titulo = input("Título del libro a eliminar: ")
        if biblioteca.eliminar_libro(titulo):
            print(f"Libro '{titulo}' eliminado correctamente.")
        else:
            print(f"Libro '{titulo}' no encontrado.")
    except ValueError as e:
        print(e)

def buscar_libro(biblioteca):
    print("\n--BUSCAR LIBRO--:")
    titulo = input("Título del libro a buscar: ")
    libro = biblioteca.buscar_libro(titulo)
    if libro:
        print("Libro encontrado:")
        print(libro)
    else:
        print(f"Libro '{titulo}' no encontrado.")

def marcar_como_prestado(biblioteca):
    print("\n--MARCAR LIBRO COMO PRESTADO--:")
    titulo = input("Título del libro a marcar como prestado: ")
    try:
        biblioteca.marcar_como_prestado(titulo)
        print(f"Libro '{titulo}' marcado como prestado.")
    except ValueError as e:
        print(e)

def devolver_libro(biblioteca):
    print("\n--DEVOLVER LIBRO--:")
    titulo = input("Título del libro a devolver: ")
    try:
        biblioteca.devolver_libro(titulo)
        print(f"Libro '{titulo}' devuelto exitosamente.")
    except ValueError as e:
        print(e)

def main():
    biblioteca = Biblioteca()
    biblioteca.cargar_libros_desde_archivo()

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            eliminar_libro(biblioteca)
        elif opcion == '3':
            print("\n--LISTA DE LIBROS--:")
            biblioteca.mostrar_libros()
        elif opcion == '4':
            buscar_libro(biblioteca)
        elif opcion == '5':
            marcar_como_prestado(biblioteca)
        elif opcion == '6':
            devolver_libro(biblioteca)
        elif opcion == '7':
            print("Guardando cambios y saliendo...")
            biblioteca.guardar_libros_en_archivo('biblioteca.txt')
            break
        else:
            print("Opción no válida. Por favor elige entre 1 y 7.")

if __name__ == "__main__":
    main()