import math
import pygame
from Color import Colors
class Position:
    def __init__(self,x,y): #Construtor
        self.x = x
        self.y = y

    def getPosition(self):
        return(self.x,self.y)

    def __eq__(self, other):
        if isinstance(other,Position):
            return self.x == other.x and self.y == other.y
        return False
    
    def draw(self, screen, diameter = 10, color = Colors.BLUE): #Desenhar
        pygame.draw.circle(screen, color, self.getPosition(),10)

    def distance(self, other):
        difx = self.x - other.x
        dify = self.y - other.y
        return math.sqrt(difx**2+dify**2)
    
    def translate(self, delta):
        self.x += delta.x
        self.y += delta.y
    
    def moveTo(self, position):
        self.x = position.x
        self.y = position.y




        
