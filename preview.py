from details import *

class Preview:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((sidebar_width, gamewindow_height * preview_height_fraction))
        self.rect = self.surface.get_rect(topright = (window_width - padding, padding))

    def run(self):
        self.display_surface.blit(self.surface, self.rect)

