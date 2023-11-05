#Создай собственный Шутер!
from pygame import *
from random import random, randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
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
        if keys_pressed[K_d] and self.rect.x < 700- 80:
            self.rect.x += self.speed
       
    def fire(self):
        bullet =Bullet('bullet.png',self.rect.centerx,self.rect.top, 15,20,-15)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        if self.rect.y > -10:
            self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroid(GameSprite):
    def update(self):
        
        self.rect.y += self.speed
        if self.rect.y >470:
            self.rect.y = 0
            self.rect.x = randint(0,635)
            self.speed = randint(1,7)
        
class Enemy(GameSprite):
    direction = 'down'
    def update(self):
        global fail
        self.rect.y += self.speed
        if self.rect.y >470:
            self.rect.y = 0
            self.rect.x = randint(0,635)
            self.speed = randint(1,7)
            fail += 1
bullets = sprite.Group() 
enemies = sprite.Group()
asteroids = sprite.Group()
for i in range(1,6):
    enemy = Enemy('ufo.png', randint(0,635),-70,65,65,randint(2,5))
    enemies.add(enemy)
for i in range(1,3):
    asteroid = Asteroid('asteroid.png', randint(0,635),-70,65,65,randint(2,5))
    asteroids.add(asteroid)
    


#class Bullet(GameSprite):
#    def __init__(self, color1,color2,color3,wallx,wally,wallwidht,wallhidht):
#        super().__init__()
#        self.color1 = color1 
#        self.color2 = color2 
#        self.hight=wallhidht
#        self.widht = wallwidht 
#        self.color3 = color3   
#        self.image = Surface((self.widht,self.hight))
#        self.image.fill((color1,color2,color3))
#        self.rect = self.image.get_rect()
#        self.rect.x = wallx
#        self.rect.y = wally
#       
#    def reset(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))

#Дисплей
window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load('galaxy.jpg'), (700,500))
background2 = transform.scale(image.load('2.jpg'), (700,500))
background3 = transform.scale(image.load('3.jpg'), (700,500))

#Cоздание обЪектовъ
player = Player('rocket.png', 300,420,30,75,15)
bullet = GameSprite('bullet.png', 600,120,1,1,0)
p = 'Победа'
l = 'Поражение'
finish = False

font.init()
font2 = font.Font(None,36)
font1 = font.Font(None,96)

score = 0
fail = 0
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
FPS = 60
clock = time.Clock()
game = True
#Циклъ игры
while  game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            
    
    if finish != True:
        
        
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        enemies.draw(window)
        enemies.update()
        asteroids.draw(window)
        asteroids.update()
        pro= font1.render('Поражение',True,(255,0,0))
        pob   = font1.render('Победа',True,(0,255,0))
        text = font2.render('Score:' + str(score),1,(45,140,200))
        window.blit(text,(10,20))
        text_fail = font2.render('Missed:' + str(fail),1,(200,200,200))
        window.blit(text_fail,(10,50))
        bullets.draw(window)
        bullets.update()
        
        gr = sprite.groupcollide(bullets,enemies,True,True)
        ar = sprite.groupcollide(bullets,asteroids,True,False)
        for c in gr:
            score += 1
            enemy = Enemy('ufo.png', randint(0,635),-70,65,65,randint(2,6))
            enemies.add(enemy)
        
        if score > 100:
           
            window.blit(background2,(0, 0))
            finish = True
            
        if fail > 90 or sprite.spritecollide(player,enemies,False) or sprite.spritecollide(player,asteroids,False):
            
            window.blit(background3,(0, 0))
            finish = True
        


        

        
        

        
       
    
    
    display.update()
    clock.tick(FPS)



#if game != False:
#    x = random.randint()
