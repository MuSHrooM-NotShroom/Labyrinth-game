from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Window.Title")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
font.init()
font = font.Font(None, 500)
win = font.render('ура  победа', True, (255, 215, 0))
loose = font.render('лох', True, (255, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
      def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (65, 65))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
      def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
      def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_a] and self.rect.x > 5:
                  self.rect.x -= self.speed
            if keys_pressed[K_d] and self.rect.x < win_width - 80:
                  self.rect.x += self.speed
            if keys_pressed[K_w] and self.rect.y > 5:
                  self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < win_height - 80:
                  self.rect.y += self.speed
class Enemy(GameSprite):
      direction = 'left'
      def update(self):
            if self.rect.x <= 470:
                  self.direction = 'right'
            if self.rect.x >= win_width - 85:
                  self.direction = 'left'
            if self.direction == 'left':
                  self.rect.x -= self.speed
            else:
                  self.rect.x += self.speed
class Wall(sprite.Sprite):
      def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
            super().__init__()
            self.color_1 = color_1
            self.color_2 = color_2
            self.color_3 = color_3
            self.width = wall_width
            self.height = wall_height
            self.image = Surface((self.width, self.height))
            self.image.fill((color_1, color_2, color_3))
            self.rect = self.image.get_rect()
            self.rect.x = wall_x
            self.rect.y = wall_y
      def draw_wall(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
player = Player('hero.png',  50, 400, 10)
enemy = Enemy('cyborg.png', win_width - 80, 280, 2)
GOLD = GameSprite('treasure.png', 500, 400, 10)
run = True
clock = time.Clock()
FPS = 60
finish = True
w1 = Wall(154, 205, 50, 120, 230, 450, 10)
w2 = Wall(154, 205, 50, 150, 150, 180, 100)
w3 = Wall(154, 205, 50, 120, 150, 100, 300)
while run:
      
      window.blit(background,(0, 0))
      for e in event.get():
            if e.type == QUIT:
                  run = False
      if finish == True:
            if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
                  kick.play()
                  window.blit(loose,(50, 100))
                  finish = False
            if sprite.collide_rect(player, GOLD):
                  money.play()
                  window.blit(win,(50, 100))
                  finish = False
            player.update()
            enemy.update()

            player.reset()
            enemy.reset()
            GOLD.reset()

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()

            display.update()
            clock.tick(FPS)
