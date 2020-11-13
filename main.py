import sys
import pygame
from settings import Settings
from battleplane import BattlePlane
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class KillBee:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("小蜜蜂")
        self.battle_plane = BattlePlane(self)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.battle_plane.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.battle_plane.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.battle_plane.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.battle_plane.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.battle_plane.blitme()
        pygame.display.flip()


    def run_game(self):
        while True:
            self._check_events()
            self.battle_plane.update()
            self._update_screen()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    bee = KillBee()
    bee.run_game()

