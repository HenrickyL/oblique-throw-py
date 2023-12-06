import pygame
from Color import Colors
class Text:
    def __init__(self, text, position, font_size=36, font_name=None):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(font_name, font_size)

    def draw(self, screen, color = Colors.BLACK):
        text_surface = self.font.render(self.text, True, color)
        screen.blit(text_surface, self.position)