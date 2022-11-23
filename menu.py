# import pygame
# import pygame_menu
# import sys
# import main


# class Menu:
#     surface = pygame.display.set_mode((600, 400))
#     select_map = 0

#     def __init__(self, game):
#         self.game = game
#         self.menu = game.menu

#     def level(self, value):  # 난이도 선택시 호출되는 함수
#         global select_map
#         print("난이도 선택값:", value)
#         if value == 1:
#             self.select_map = 1
#         elif value == 2:
#             self.select_map = 2

#     def start(self):  # 게임시작 선택시 호출되는 함수
#         print("게임시작")
#         self.run()

#     def quit(self):
#         pygame.quit()
#         sys.exit()

#     def run(self):
#         surface = pygame.display.set_mode((600, 400))

#         t = pygame_menu.themes.THEME_DARK
#         t.widget_font = pygame.font.SysFont("gothic", 30)

#         menu = pygame_menu.Menu("DOOM", 400, 300, theme=t)
#         menu.add.selector("MAP ", [("1", 1), ("2", 2)], onchange= self.level)
#         menu.add.button("START", self.start)
#         menu.add.button("QUIT", self.quit)
#         menu.mainloop(surface)
#         # menu
