📚 Sistema de Gestión de Biblioteca
Sistema de gestión de biblioteca desarrollado en Python con POO (Programación Orientada a Objetos) para Evaluación de Módulo 4, Bootcamp Full Stack Python.
--
🚀 Instalación y Uso

```bash
# Clonar o descargar el proyecto
git clone [repositorio-url](https://github.com/too0oori/Evaluacion_Modulo_4)

# Navegar a la carpeta
cd gestor_biblioteca

# Ejecutar el programa
python gestor_biblioteca.py
```
--

📋 Funcionalidades

✅ Agregar libros (físicos y digitales)
✅ Eliminar libros
✅ Buscar libros por título
✅ Marcar como prestado/devolver
✅ Persistencia de datos automática
✅ Visualizar todos los libros

--

🗂️ Estructura del Proyecto
```bash
📦 gestor_biblioteca
 ┣ 📜 libro.py              # Clases Libro y LibroDigital
 ┣ 📜 biblioteca.py         # Clase Biblioteca (lógica principal)
 ┣ 📜 gestor_biblioteca.py  # Menú y programa principal
 ┣ 📜 biblioteca.txt        # Almacenamiento de datos (se crea automáticamente)
 ┗ 📜 README.md             # Este archivo
  ┗ 📜 Diagrama_Clases.

```
 --

 💻 Ejemplo de Uso

```bash
 Bienvenido al gestor de biblioteca
1. Agregar libro
2. Eliminar libro
3. Ver todos los libros
4. Buscar libro
5. Marcar libro como prestado
6. Devolver libro
7. Salir

Seleccione una opción: 1

--AGREGAR LIBRO--:
¿Es un libro digital? (s/n): n
Título: Cien años de soledad
Autor: Gabriel García Márquez
Año de publicación: 1967
Libro 'Cien años de soledad' agregado correctamente.
```
--
Características Técnicas

POO: Uso de clases, herencia y polimorfismo
Persistencia: Almacenamiento en archivo de texto
Manejo de errores: Validaciones y excepciones
Encoding UTF-8: Soporte para acentos y caracteres especiales

--

📝 Requisitos

Python 3.6+
--

Autor
Sofía Lagos C.