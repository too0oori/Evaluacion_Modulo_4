
class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.ano_publicacion}) - {estado}"
    
    def libro_prestado(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado.")
        self.disponible = False
    
    def devolver(self):
        self.disponible = True

class LibroDigital(Libro):
    def __init__(self, titulo, autor, ano_publicacion, formato):
        super().__init__(titulo, autor, ano_publicacion)
        self.formato = formato
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.ano_publicacion}) - Formato: {self.formato} - {estado}"