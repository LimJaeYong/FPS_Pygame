import pygame as pg
from settings1 import *

class SpriteObject:
    def __init__(self, game, path = 'resources/sprites/static_sprites/candlebra.png', pos = (10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_height() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        
    def get_sprite_protjection(self):
        proj = SCREEN_DIST / self.norm_dist
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        
        image = pg.transform.scal(self.image, (proj_width, proj_height))
        
        self.sprite_half_width = proj_width / 2 #구조물 중간 위치
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 #화면 밖으로 나가지 않는 위치
        
        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))
    
    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        
        #인수가 2개인 역탄젠트
        #플레이어가 구조물을 바라보는 각 계산
        self.theta = math.atan2(dx,dy)
        
        #플레이어 앵글
        #세타와 플레이어 방향각의 차이  
        delta = self.theta = self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or ( dx < 0 and dy < 0):
            delta += math.tau #tau = 2pi
            
        #광선이 몇개 필요한지
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE
        
        #구조물 크기 결정을 위한 거리계산
        self.dist = math.hypot(dx, dy) #직각삼각형 빗면 계산
        self.norm_dist = self.dist * math.cos(delta)
        #게임 성능 향상
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()
    
    def update(self):   
        self.get_sprite()