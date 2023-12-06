import pygame
from Game import Game
from  Color import Colors
import sys

class Engine:
    def __init__(self, width, height, title = "Title"):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.title = title
        self.background = Colors.GRAY

    def run(self, fixed_fps=True, fps=60):
        running = True
        pygame.init()
        delta_time = 0
        pygame.display.set_caption(self.title)
        while running:
            self.screen.fill(self.background)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.game.handle_event(events)

            if fixed_fps:
                self.game.update(1 / fps)
                self.game.draw(self.screen)
                pygame.display.flip()
                self.clock.tick(fps)
            else:
                current_time = pygame.time.get_ticks()
                self.game.update(delta_time / 1000.0)
                self.game.draw(self.screen)
                pygame.display.flip()
                delta_time = pygame.time.get_ticks() - current_time
                
            # pygame.display.set_caption(f"[{delta_time}]" +self.title)
                
        pygame.quit()
        sys.exit()