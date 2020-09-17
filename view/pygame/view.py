import pygame
from view.globalVariables import *
from view.pygame.button import Button
from collections import OrderedDict 

class Visualizer:

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(SIZE)

        pygame.display.set_caption("Sorting Visualizer")

        self.clock = pygame.time.Clock()

    def button_set(self):

        sorting_algoritms = { "Bubble" : 0,
                              "Insertion" : 150,
                              "Merge" : 300,
                              "Selection" : 450,
                              "Quick" : 600,
                              "Heap" : 750
        }

        for algorithm, distance in sorting_algoritms.items():
            button_algorithm = Button(
                BLUE,
                WIDTH/16 - BUTTON_WIDTH/2 + distance,
                HEIGHT/10 - BUTTON_HEIGHT,
                BUTTON_WIDTH,
                BUTTON_HEIGHT,
                f"{algorithm} Sort"
            )
            button_algorithm.draw(self.screen, WHITE)

    def main_loop(self):
        while True:

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
            
        
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLUE, (0, 0, WIDTH, HEIGHT // 8))

            self.button_set()

            pygame.display.flip()

            self.clock.tick(FPS)