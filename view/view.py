import pygame
from code.globalVariables import *

class Visualizer:

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(SIZE)

        pygame.display.set_caption("Sorting Visualizer")

        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True:

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
            
        
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLUE, (0, 0, WIDTH, HEIGHT // 8))

            pygame.display.flip()

            self.clock.tick(FPS)