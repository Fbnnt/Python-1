#Fabian Vargas

class libro:
    def __init__(self, titulo, autor, paginas, genero, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.copias_disponibles = copias_disponibles
    
    def atributos(self):
        print(self.titulo, ":",sep=" ")
        print("Autor:", self.autor)
        print("Paginas:", self.paginas)
        print("Genero:", self.genero)
        print("Copias disponibles:", self.copias_disponibles)
    
    def incrementar_copias(self, nuevas_copias):
        self.copias_disponibles = self.copias_disponibles+nuevas_copias
    
    def esta__disponible(self):
        self.copias_disponibles = 0

    def agotado(self):
        self.copias_disponibles == 0
        print(self.titulo, "está agotado")
    def prestar (self, copias=1):
        if self.copias_disponibles >= copias:
            self.copias_disponibles -= copias
            print(f"Has prestado {copias} copias(s) de '{self.titulo}'.")
        else:
            print(f"No hay suficientes copias disponibles '{self.titulo}'.")

mi_libro = libro("El Principito", "Antoine de Saint-Exupéry", 96, "ficción", 10)

print("\n ====Prestar copias====")
mi_libro.prestar(2)
mi_libro()
#¿Inizialisame la clase sin inizialisarla?
#¿Para que sirve pass?
#¿como entregarle los valores a una clase?
#¿Como se llaman la funcion dentro de una clase?
#¿Como accedo a los valores de un objeto?
#¿que es self? El parametro de la misma clase
#¿como creamos el metodo de atributos de una clase?
#¿como llamamos al metodo de atrivutos de una clase?
#¿?