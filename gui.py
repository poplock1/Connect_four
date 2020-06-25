import pygame


class Button(object):
    def __init__(self, x, y, width, height, text_color, background_color, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont('Comic Sans MS', font_size)
        self.text = text
        self.text_color = text_color
        self.text = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.background_color = background_color

    def draw(self, display):
        self.button = pygame.draw.rect(
            display, self.background_color, (self.rect), 0)
        display.blit(self.text, (self.rect.centerx - self.text_rect.width //
                                 2, self.rect.centery - self.text_rect.height//2))
        pygame.draw.rect(display, self.text_color, self.rect, 3)


class TextWindow(object):
    def __init__(self, x, y, width, height, text_color, text, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont('Comic Sans MS', font_size)
        self.text = text
        self.text_color = text_color
        self.text = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text.get_rect()

    def draw(self, display, align="center"):
        if align == "center":
            display.blit(self.text, (self.rect.centerx - self.text_rect.width//2,
                                     self.rect.centery - self.text_rect.height//2))
        elif align == "left":
            display.blit(
                self.text, (self.rect.x, self.rect.centery - self.text_rect.height//2))
        elif align == "right":
            display.blit(self.text, (self.rect.x + self.rect.width -
                                     self.text_rect.width, self.rect.centery - self.text_rect.height//2))
