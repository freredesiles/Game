import pygame as pg
import manage as ma
import fonctions as fc
import all_class as ac
import random as rd
import time
import os

os.chdir("/home/martin/Documents/gitproject")

pg.init()
taille_fenêtre = (800, 400)
screen_m = pg.display.set_mode(taille_fenêtre)
player = ac.Player("BIGPROJECTRPG/image/Roman.png", 32, 64, 8, 256)
enemy = ac.Enemy("BIGPROJECTRPG/image/Roman.png", 32, 64, 8, 256, posy=50)
fireball = ac.Spell("BIGPROJECTRPG/image/Fireball.png", 16, 16, 6, 16)
game = True
gamemenu = True
pg.key.set_repeat(20, 20)
play = ac.Contenu("PLAY", 50, (255, 255, 255), taille_fenêtre)
quitt = ac.Contenu("QUIT", 50, (255, 255, 255), taille_fenêtre, y=50)
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


while game:

    event = pg.event.poll()

    if event.type == pg.QUIT:

        game = False

    if event.type == pg.KEYDOWN:

        if event.key == pg.K_DOWN:
            player.y = 5
            player.key = pg.K_DOWN
            player.update_character(screen_m, (255, 255, 255), 0)

        elif event.key == pg.K_UP:

            player.y = -5
            player.key = pg.K_UP
            player.update_character(screen_m, (255, 255, 255), 1)

        elif event.key == pg.K_RIGHT:
            player.x = 5
            player.key = pg.K_RIGHT
            player.update_character(screen_m, (255, 255, 255), 2)

        elif event.key == pg.K_LEFT:

            player.x = -5
            player.key = pg.K_LEFT
            player.update_character(screen_m, (255, 255, 255), 3)

        elif event.key == pg.K_a:

            fireball.x = 10
            fireball.key = pg.K_a
            player.cast_spell(fireball, screen_m)

    elif event.type == pg.KEYUP:

        player.index = player.nb_sprite - 1

        if player.key == pg.K_DOWN:

            player.update_character(screen_m, (255, 255, 255), 0)

        elif player.key == pg.K_UP:

            player.update_character(screen_m, (255, 255, 255), 1)

        elif player.key == pg.K_RIGHT:

            player.update_character(screen_m, (255, 255, 255), 2)

        elif player.key == pg.K_LEFT:

            player.update_character(screen_m, (255, 255, 255), 3)

    clock.tick(60)






























