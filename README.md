# Evaluacion_Modulo_4


Evaluación del módulo

Objetivo

En esta actividad, desarrollarás un sistema de gestión de biblioteca utilizando el paradigma de programación orientada a objetos. Crearás clases para representar libros y una biblioteca, manejando atributos, métodos y la colaboración entre objetos. Además, el sistema deberá permitir almacenar información sobre los libros en un archivo para persistencia de datos.

Contexto

Imagina que eres un desarrollador de software encargado de crear una pequeña aplicación para gestionar los libros de una biblioteca. Esta biblioteca puede tener varios libros, y se deben poder agregar, eliminar y listar libros. Además, debes guardar la información de los libros en un archivo para que, cuando el programa se cierre, los datos no se pierdan.

Para lograr esto, utilizarás las ventajas de la orientación a objetos, como la encapsulación, la abstracción y el polimorfismo, y también aplicarás el manejo de archivos para guardar la información en un archivo de texto.

Requisitos del Proyecto

    Clases y Objetos

        Crear una clase Libro con los siguientes atributos:

            Título

            Autor

            Año de publicación

            Estado (disponible o prestado)

        Crear una clase Biblioteca que contenga los siguientes métodos:

            Agregar un libro

            Eliminar un libro por su título

            Listar todos los libros disponibles

            Buscar un libro por su título

            Marcar un libro como prestado

            Devolver un libro prestado

    Métodos de la clase Libro

        Incluir un método constructor para inicializar los atributos del libro.

        Crear métodos accesores (getters) y mutadores (setters) para los atributos.

        Incluir un método __str__ para representar un libro en formato legible (por ejemplo: "Título: El Quijote, Autor: Cervantes, Año: 1605, Estado: Disponible").

    Colaboración entre objetos

        La clase Biblioteca debe gestionar una lista de objetos Libro.

        Implementar la colaboración entre objetos creando un método en la clase Biblioteca que recorra la lista de libros y ejecute operaciones sobre ellos (como marcar libros como prestados o devolverlos).

    Manejo de Excepciones

        Utiliza el manejo de excepciones para capturar errores, como intentar eliminar un libro que no existe en la lista o marcar un libro como prestado que ya está prestado.

    Persistencia con Archivos

        La información de los libros debe almacenarse en un archivo llamado biblioteca.txt.

        El archivo debe contener los detalles de los libros (por ejemplo, título, autor, estado).

        Al iniciar el programa, los libros deben cargarse desde el archivo.

        Al finalizar el programa, los cambios en los libros deben guardarse en el archivo.

    Modos de archivo

        El programa debe ser capaz de leer y escribir en el archivo biblioteca.txt en los modos correspondientes:

            Lectura al iniciar el programa para cargar los libros.

            Escritura para guardar los cambios al finalizar el programa.

    Uso de polimorfismo y herencia

        Crea una clase LibroDigital que herede de la clase Libro y agregue un atributo adicional formato (ej. PDF, ePub).

        Sobreescribe el método __str__ para mostrar también el formato del libro digital.

    Diagramas de clase

        Dibuja un diagrama de clases que muestre la relación entre Libro, LibroDigital y Biblioteca.

        El diagrama debe incluir los atributos y métodos de cada clase, así como la herencia entre Libro y LibroDigital.

Ejemplo de Uso

Cuando el usuario ejecute el programa, verá un menú como el siguiente:

--- Gestor de Biblioteca ---
1. Agregar libro
2. Eliminar libro
3. Ver todos los libros
4. Buscar libro
5. Marcar libro como prestado
6. Devolver libro
7. Salir
Elige una opción:

Entregables del Proyecto

    Archivo Python (gestor_biblioteca.py) con el código del programa.

    Archivo biblioteca.txt con los libros almacenados.

    Documento breve (README.txt o README.md) explicando cómo ejecutar el programa.

    Diagrama de clases que representa la estructura del sistema.

