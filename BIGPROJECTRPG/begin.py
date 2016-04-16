import pygame as pg
import manage as ma
import fonctions as fc
import all_class as ac
import random as rd
import time
import os

os.chdir("/home/martin/Documents/gitproject")

pg.init()
screen_size = (400, 200)
screen_m = pg.display.set_mode(screen_size)
player = ac.Player("BIGPROJECTRPG/image/Roman.png", 32, 64, 8, 256)
enemy = ac.Enemy("BIGPROJECTRPG/image/Roman.png", 32, 64, 8, 256, posx=200)
game = True
gamemenu = True
pg.key.set_repeat(20, 20)
play = ac.Contenu("PLAY", 50, (255, 255, 255), screen_size)
quitt = ac.Contenu("QUIT", 50, (255, 255, 255), screen_size, y=50)
menu = [play, quitt]
clock = pg.time.Clock()

while gamemenu:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        pos = pg.mouse.get_pos()
        screen_m.fill((0, 0, 0))

        for index in range(len(menu)):

            menu[index].collision(pos[0], pos[1], event)
            booléen = menu[index].surbrillance()
            m = menu[index]
            screen_m.blit(m.text_render, m.rectt)
            m.rect = pg.Rect(m.x, m.y, m.size[0]+10, m.size[1]+10)
            pg.display.update(m.rect)

            if event.type == pg.MOUSEBUTTONDOWN:

                if booléen:
                    if index == 1 or event.type == pg.QUIT:

                        pg.quit()

                    elif index == 0:

                        gamemenu = False

        pg.event.clear()

screen_m.fill((255, 255, 255))
pg.display.flip()
group_spells = pg.sprite.Group()
index = 0
x = 0
y = 0
list_sprite = [enemy, player]

while game:

    event = pg.event.poll()

    if event.type == pg.QUIT:

        game = False

    if event.type == pg.KEYDOWN:

        if event.key == pg.K_DOWN:

            index = 0
            player.move(y=5)
            y = 5  # Used for the spells'move
            x = 0

        elif event.key == pg.K_UP:

            index = 1
            player.move(y=-5)
            y = -5
            x = 0

        elif event.key == pg.K_RIGHT:

            index = 2
            player.move(x=5)
            x = 5
            y = 0

        elif event.key == pg.K_LEFT:

            index = 3
            player.move(x=-5)
            x = -5
            y = 0

        elif event.key == pg.K_a:

            newspell = player.cast_spell("BIGPROJECTRPG/image/Fireball.png", 16, 16, 6, 16, x, y, "Fireball", 30, player
                                         )

            if ac.Spell.time_to_cast:

                ac.Spell.spell_time["Fireball"] = pg.time.get_ticks()
                list_sprite.append(newspell)

            player.index = player.nb_sprite - 1

    else:

        player.index = player.nb_sprite - 1

    enemy.move(y=1)

    list_sprite = fc.sprite_collision(list_sprite, screen_m, (255, 255, 255))
    list_sprite = fc.check_alive(list_sprite, screen_m, (255, 255, 255))
    fc.update_sprite(list_sprite, screen_m, (255, 255, 255), index)

    clock.tick(40)
































