import pygame
from Position import Position
from Vector import Vector
from  Color import Colors
from Text import Text
import math


class Game:
    def __init__(self):
        #valores iniciais
        self.gravity = 0.98
        self.angle_graus = 45
        self.power = 20
        self.start = False
        self.positionInitial = Position(50, 500)
        self.position = Position(50, 500)
        self.position_color = Colors.RED
        
        #variable
        self.speed = None
        self.H_aux = self.positionInitial.y
        self.distance_aux = self.positionInitial.x
        self.H_max = 0
        self.distance = 0
        self.points = []
        
        #passos
        self.gravity_tick = 0.01
        self.power_tick = 0.5
        self.t_tick = 20
        
        


    def update(self, delta_time):
        if self.start:
            #vetor aceleracao sendo aplicado ao vetor_speed
            # tem que ir sobrescrevendo para cada Delta_t
            if(self.positionInitial.y >= self.position.y):
                self.speed = self.speed + Vector.Down*self.gravity
                self.position.translate(self.speed)
                
                if(self.H_aux > self.position.y):
                    self.H_aux = self.position.y
                else:
                    self.H_max = self.positionInitial.y -  self.H_aux
                
            else:
                self.start = False
                self.position_color = Colors.GREEN
                self.distance = self.position.x - self.positionInitial.x
                



    def draw(self, screen):
        posY = 530  
        
        #desenha a posição
        self.position.draw(screen, color=self.position_color)
        x = f"{self.position.x:03.1f}"
        y = f"{self.position.y:03.1f}"
        Text(f'P = ({x}, {y})', (0,posY+30) ).draw(screen, color=Colors.RED)
        
        posX = 620
        #desenha gravidade
        Text(f'G = {self.gravity:.2f}', (posX,0) ).draw(screen)
        #desenha angulo
        Text(f'angle = {str(self.angle_graus).zfill(2)}º', (posX,20) ).draw(screen)
        #desenha potencia
        Text(f'power = {self.power}', (posX,40) ).draw(screen)
        
        #desenha H_max
        Text(f'H_max = {self.H_max:02.2f}', (600,posY) ).draw(screen)
        Text(f'Distance = {self.distance:02.2f}', (600,posY+30) ).draw(screen)
        
        for point in self.points:
            point.draw(screen ,color=Colors.BLACK)
        
        #desenha a posiçao inicial
        self.positionInitial.draw(screen ,color=Colors.BLUE)
        x = str(self.positionInitial.x)
        y = str(self.positionInitial.y)
        Text(f'Pi = ({x}, {y})', (0,posY) ).draw(screen)
        


    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.resetAux()
                    self.calcVector()
                    self.points.append(self.position)
                    self.position = Position(self.positionInitial.x, self.positionInitial.y)
                    self.start = True
        if(not events):
            keys = pygame.key.get_pressed()
            self.handle_keys(keys)

    #inputs
    def handle_keys(self, keys):
        
        if keys[pygame.K_r]:
            self.reset()
            
        if keys[pygame.K_RIGHT]:
            if(self.power < 50):
                self.power += self.power_tick
        if keys[pygame.K_LEFT]:
            if(self.power > 0 ):
                self.power -= self.power_tick   
                
        if keys[pygame.K_w]:
            self.gravity += self.gravity_tick
        if(keys[pygame.K_UP]):
            if(self.angle_graus < 90):
                self.angle_graus += 1

        if keys[pygame.K_s]:
            self.gravity -= self.gravity_tick
        if keys[pygame.K_DOWN]:
            if(self.angle_graus > 0):
                self.angle_graus -= 1
                
                
    def reset(self):
       #valores iniciais
        self.gravity = 0.98
        self.angle_graus = 45
        self.power = 20
        self.start = False
        self.positionInitial = Position(50, 500)
        self.position = Position(50, 500)
        
        #variable
        self.speed = None
        self.resetAux()
        self.H_max = 0
        self.distance = 0
        self.points = []
        
        self.calcVector()

    def calcVector(self):
        #definir outros
        self.position_color = Colors.RED
        angleRad = self.getAngleRad(self.angle_graus)
        vx = math.cos(angleRad) * self.power
        vy = math.sin(angleRad) * self.power
        self.speed = Vector(vx,-vy)
        
    def getAngleRad(self, angle):
        return angle * math.pi / 180


    def resetAux(self):
        self.H_aux = self.positionInitial.y
        self.distance_aux = self.positionInitial.x
    