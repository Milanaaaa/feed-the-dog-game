import pygame
import random


def inter(x1, y1, x2, y2, db1, db2):
    self_x1 = x1
    self_x2 = x1 + db1
    self_y1 = y1
    self_y2 = y1 + db1

    other_x1 = x2
    other_x2 = x2 + db2
    other_y1 = y2
    other_y2 = y2 + db2

    s1 = (self_x1 > other_x1 and self_x1 < other_x2) or (self_x2 > other_x1 and self_x2 < other_x2)
    s2 = (self_y1 > other_y1 and self_y1 < other_y2) or (self_y2 > other_y1 and self_y2 < other_y2)
    s3 = (other_x1 > self_x1 and other_x1 < self_x2) or (other_x2 > self_x1 and other_x2 < self_x2)
    s4 = (other_y1 > self_y1 and other_y1 < self_y2) or (other_y2 > self_y1 and other_y2 < self_y2)
    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        return True
    else:
        return False


class Meals:
    def __init__(self, x, y, image, cat):
        self.x = x
        self.y = y
        self.img = pygame.image.load(image)
        self.shape = pygame.Surface((40, 40))
        self.cat = cat


pygame.init()

window = pygame.display.set_mode((600, 600))
screen = pygame.Surface((600, 600))
player = pygame.Surface((60, 60))

player.set_colorkey((255, 255, 255))

img_p = pygame.image.load('taksa_game_images/taksa.png')
img_bg = pygame.image.load('taksa_game_images/grass.png')
meals_pics = ['taksa_game_images/sausage.png', 'taksa_game_images/bone.png', 'taksa_game_images/cutlet.png',
              'taksa_game_images/spider.png', 'taksa_game_images/bad_bone.png']

count = 0
bad_count = 0
my_font = pygame.font.SysFont('monospace', 15)
string = my_font.render('Поймано: ' + str(count), 0, (0, 255, 0))
string2 = my_font.render('Пропущено: ' + str(bad_count), 0, (255, 0, 0))

z_x = 0

z_y = 0

p_x = 200
p_y = 300

done = False
game_over = False

meal = []

while not done:
    if not game_over and len(meal) < 1:
        z_x = 600
        z_y = random.randrange(540)
        pic = random.choice(meals_pics)
        cat = True
        if pic == 'taksa_game_images/spider.png' or pic == 'taksa_game_images/bad_bone.png':
            cat = False
        meal.append(Meals(z_x, z_y, pic, cat))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            p_y += 15
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            p_y -= 15
            # if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:

            # if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            #     p_x -= 10
            # if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            #     p_x += 10
    for z in meal:
        if inter(z.x, z.y, p_x, p_y, 40, 60):
            if z.cat is False:
                count -= 2
            strike = False
            z.x = 1000
            z.y = 1000

            count += 1
            meal.pop(meal.index(z))
            string = my_font.render('Поймано: ' + str(count), 0, (0, 255, 0))

    for m in meal:
        m.x -= 0.1
        if m.x < 0:
            m.x = 1000
            m.y = 1000
            meal.pop(meal.index(m))
            if z.cat is True:
                bad_count += 1
            string2 = my_font.render('Пропущено: ' + str(bad_count), 0, (255, 0, 0))
    if bad_count > count:
        game_over = True
    if game_over:
        string3 = my_font.render('ВЫ ПРОИГРАЛИ', 0, (255, 0, 0))

    screen.blit(img_bg, (0, 0))
    player.blit(img_p, (0, 0))

    for m in meal:
        m.shape.set_colorkey((255, 255, 255))
        m.shape.blit(m.img, (0, 0))
        screen.blit(m.shape, (m.x, m.y))

    screen.blit(string, (0, 50))
    screen.blit(string2, (0, 70))
    if game_over:
        screen.blit(string3, (0, 90))
    screen.blit(player, (p_x, p_y))
    window.blit(screen, (0, 0))
    pygame.display.update()
    if game_over:
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            count = 0
            bad_count = 0
            my_font = pygame.font.SysFont('monospace', 15)
            string = my_font.render('Поймано: ' + str(count), 0, (0, 255, 0))
            string2 = my_font.render('Пропущено: ' + str(bad_count), 0, (255, 0, 0))
            p_x = 200
            p_y = 300
            done = False
            game_over = False
            meal = []

pygame.quit()
