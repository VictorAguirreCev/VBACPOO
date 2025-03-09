class Libro:
    """
    Representa un libro en la biblioteca.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} de {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    """
    Representa un usuario de la biblioteca.
    """
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # Identificador único
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    """
    Sistema de gestión de biblioteca digital.
    """
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios_registrados = {}  # Diccionario con ID de usuario como clave
        self.historial_prestamos = []  # Lista para registrar préstamos

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        """Elimina un libro de la biblioteca por su ISBN."""
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, user_id):
        """Elimina un usuario de la biblioteca."""
        if user_id in self.usuarios_registrados:
            del self.usuarios_registrados[user_id]
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        """Presta un libro a un usuario."""
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[user_id]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.historial_prestamos.append((usuario, libro))
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        """Devuelve un libro a la biblioteca."""
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
        print("Libro no encontrado en los préstamos del usuario.")

    def buscar_libro(self, criterio, valor):
        """Busca libros por título, autor o categoría."""
        resultados = []
        for libro in self.libros_disponibles.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower()) or \
               (criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower()) or \
               (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def listar_libros_prestados(self, user_id):
        """Lista los libros actualmente prestados a un usuario."""
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# --- PRUEBAS DEL SISTEMA ---

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "0987654321")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("Ana Gómez", "U002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro
biblioteca.prestar_libro("U001", "1234567890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver el libro
biblioteca.devolver_libro("U001", "1234567890")

# Buscar un libro por autor
biblioteca.buscar_libro("autor", "Gabriel García Márquez")

# Eliminar un libro
biblioteca.eliminar_libro("0987654321")

# Dar de baja un usuario
biblioteca.dar_de_baja_usuario("U002")
