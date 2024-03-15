import pygame


class Ship():

    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = si_game.settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
