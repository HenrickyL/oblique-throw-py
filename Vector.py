import math
class Vector:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        else:
            raise ValueError("Não é possível dividir por zero.")
        
Vector.Forward = Vector(0, -1)  # Move para cima (direção negativa ao longo do eixo y)
Vector.Backward = Vector(0, 1)  # Move para baixo (direção positiva ao longo do eixo y)
Vector.Up = Vector(0, -1)  # Move para cima (direção negativa ao longo do eixo y)
Vector.Down = Vector(0, 1)  # Move para baixo (direção positiva ao longo do eixo y)
Vector.Left = Vector(-1, 0)  # Move para a esquerda (direção negativa ao longo do eixo x)
Vector.Right = Vector(1, 0)  # Move para a direita (direção positiva ao longo do eixo x)
Vector.Zero = Vector(0, 0)  # Vetor nulo
Vector.One = Vector(1, 1)  # Vetor com coordenadas (1, 1)
