from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed):
        super().__init__()

        self.pimage = transform.scale(image.load(pimage), (65, 65))

        self.rect = self.pimage.get_rect()
        self.speed = speed

        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.pimage, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

    def down(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

    def left(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

    def right(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < win_width - self.rect.width:
            self.rect.x += self.speed


class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x > win_width - self.rect.width:
            self.direction = 'left'
        if self.rect.x < win_width * 0.3:
            self.direction = 'right'

        if self.direction == 'left':
            self.rect.x -= self.speed

        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3 
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



wall1 = Wall(86, 2, 31, 60, 60, 20, 350)
wall2 = Wall(86, 2, 31, 60, 60, 550, 20)
wall3 = Wall(86, 2, 31, 600, 60, 20, 350)
wall4 = Wall(86, 2, 31, 170, 150, 20, 350)
wall5 = Wall(86, 2, 31, 170, 150, 140, 20)
wall6 = Wall(86, 2, 31, 300, 150, 20, 100)
wall7 = Wall(86, 2, 31, 300, 250, 120, 20)
wall8 = Wall(86, 2, 31, 400, 150, 20, 100)
wall9 = Wall(86, 2, 31, 400, 150, 120, 20)
wall10 = Wall(86, 2, 31, 500, 150, 20, 260)

win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))

background = transform.scale(image.load("trees.jpg"), (win_width, win_height))

display.set_caption("Лабіринт")


player = Player('hedgehog.png', 10, win_height-80, 4)
enemy = Enemy('brick.png', win_width-80, 80, 2)
final = GameSprite('milk.png', win_width-80, win_height-80, 0)


game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

while game:
    window.blit(background, (0, 0))


    player.update() 
    player.left()
    player.right()
    player.down()


    enemy.update()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall10.draw_wall()


    player.draw()
    enemy.draw()
    final.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(player, wall1) or \
    sprite.collide_rect(player, wall2) or \
    sprite.collide_rect(player, wall3) or \
    sprite.collide_rect(player, wall4) or \
    sprite.collide_rect(player, wall5) or \
    sprite.collide_rect(player, wall6) or \
    sprite.collide_rect(player, wall7) or \
    sprite.collide_rect(player, wall8) or \
    sprite.collide_rect(player, wall9) or \
    sprite.collide_rect(player, wall10) or \
    sprite.collide_rect(player, enemy):
        kick.play()
        player.rect.x = 100
        player.rect.y = 400
    if sprite.collide_rect(player, final):
        time.delay(1000)
        money.play()
        game = False

    
    display.update()
    clock.tick(FPS)