from details import *
from random import choice

from timer import Timer


class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((gamewindow_width, gamewindow_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.sprites = pygame.sprite.Group()

        # lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((139,131,134))
        self.line_surface.set_colorkey((139,131,134))
        self.line_surface.set_alpha(120)

        # tetromino
        self.tetromino = Tetromino(choice(list(Tetrominos.keys())), self.sprites)

        # timer
        self.timers = {
            'vertical move': Timer(update_start_speed, True, self.move_down)
            }
        self.timers['vertical move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        print('timer')
        self.tetromino.move_down()

    def draw_grid(self):

        for col in range(1, colums):
            x = col * cells
            pygame.draw.line(self.surface, linecolor, (x,0), (x,self.surface.get_height()), 1)

        for row in range(1, rows):
            y = row * cells
            pygame.draw.line(self.surface, linecolor, (0,y), (self.surface.get_width(), y))

        self.surface.blit(self.line_surface, (0,0))

    def run(self):
        
        #update timer
        self.timer_update()

        # drawing
        self.surface.fill((20,20,20))
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (padding, padding))
        pygame.draw.rect(self.display_surface, linecolor, self.rect, 2, 2)
        
class Tetromino:
    def __init__(self, shape, group):

        # setup
        self.block_positions = Tetrominos[shape]['shape']
        self.color = Tetrominos[shape]['color']

        # create blocks
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]

    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):

        # general
        super().__init__(group)
        self.image = pygame.Surface((cells, cells))
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) +pygame.Vector2(colums // 2, 5)
        x = self.pos.x * cells
        y = self.pos.y * cells
        self.rect = self.image.get_rect(topleft = (x,y))