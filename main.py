from details import *

#components
from gamewindow import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):
        
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PennysTetris")

        # components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            
            self.display_surface.fill((20, 20, 20))

            self.game.run()
            self.score.run()
            self.preview.run()

            pygame.display.update()
            self.clock.tick() 

if __name__ == '__main__':
    main = Main()
    main.run()