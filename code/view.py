import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 128)

class Visualizer:

    HEIGHT = 800
    WIDTH = 1600

    SIZE = (WIDTH, HEIGHT)
    TOP_RECTANGLE = (WIDTH, HEIGHT//10)

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.SIZE)

        pygame.display.set_caption("Sorting Visualizer")

        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True:

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
            
        
            self.screen.fill(WHITE)

            pygame.draw.rect(self.screen, BLUE, (0, 0, self.WIDTH, self.HEIGHT // 8))

            pygame.display.flip()

            self.clock.tick(60)

if __name__ == '__main__':
    app = Visualizer()
    app.main_loop()