import pygame
import sys
import pygame_menu
from settings1 import *
from map1 import *
from raycasting import *
from player1 import *
from object_renderer import *
from sprite_object1 import *
from object_handler import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)  # 마우스 포인트 숨기기
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        # self.static_sprite = SpriteObject(self)
        # self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)

    def update(self):
        self.player.update()
        self.raycasting.update()

        # object_renderer 완성 후 실행
        # self.static_sprite.update()
        # self.animated_sprite.update()

        self.object_handler.update()

        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        # self.clock.tick(0)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    # menu
    '''
    def set_difficulty(value, difficulty):
        global WIDTH, HEIGHT
        if difficulty == 1:
            WIDTH, HEIGHT = 10, 10
            HEIGHT = 10
        elif difficulty == 2:
            WIDTH, HEIGHT = 15, 10
        else:
            WIDTH, HEIGHT = 20, 15

    def start_the_game():
        global CHECKED
        global OPEN_COUNT
        global SURFACE
        global TIMER
        SURFACE = pygame.display.set_mode([WIDTH*SIZE+300, HEIGHT*SIZE])
        CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        OPEN_COUNT = 0
        TIMER = 1000
        game.run()

    def show_start_menu():
        # print(pygame.font.get_fonts())
        hanfont = pygame.font.SysFont("malgungothic", 30)
        #gamefont = pygame_menu.font.FONT_8BIT
        t = pygame_menu.themes.THEME_BLUE.copy()
        t.widget_font = hanfont
        menu = pygame_menu.Menu("Menu", 500, 300, theme=t)
        menu.add.selector("난이도", [("하", 1), ("중", 2), ("상", 3)],onchange=set_difficulty)
        menu.add.button("게임 시작", start_the_game)
        menu.add.button("게임 종료", pygame_menu.events.EXIT)
        menu.mainloop(SURFACE)

    def show_restart_menu(message):
        hanfont = pygame.font.SysFont("malgungothic", 30)
        t = pygame_menu.themes.THEME_BLUE.copy()
        t.widget_font = hanfont
        menu = pygame_menu.Menu("Menu", 500, 300, theme=t)
        menu.add.button("다시 시작", show_start_menu)
        menu.add.button("게임 종료", pygame_menu.events.EXIT)
        menu.mainloop(SURFACE)
    '''
    ## end of menu
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
