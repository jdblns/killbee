import pygame


class BattlePlane:
    def __init__(self, kill_bee):
        self.screen = kill_bee.screen
        self.screen_rect = kill_bee.screen.get_rect()
        self.settings = kill_bee.settings

        self.image = pygame.image.load('images/battle_plane.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.bp_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.bp_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)