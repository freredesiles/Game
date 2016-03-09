import pygame as pg
import Game.BIGPROJECTRPG.all_class as ac


sprite_height = 64
sprite_width = 32
pg.init()
taille_fenêtre = (1000, 800)
screen = pg.display.set_mode(taille_fenêtre)  # Taille de la fenêtre
player = ac.Personnage("image/Roman.png", sprite_height, sprite_width, 8, 256)
game_exit = True
game_menu = True
play = ac.Contenu("Play", 60, (255, 255, 255), taille_fenêtre)
options = ac.Contenu("Options", 60, (255, 255, 255), taille_fenêtre, y=50)
quitter = ac.Contenu("Quit", 60, (255, 255, 255), taille_fenêtre, y=100)
menu = [play, options, quitter]

while game_menu:

    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        screen.fill((0, 0, 0))

        for index in range(len(menu)):

            menu[index].collision(pos[0], pos[1], event)
            booléen = menu[index].surbrillance()
            m = menu[index]
            screen.blit(m.text_render, m.rect)
            m.rect = pg.Rect(m.x, m.y, m.size[0]+10, m.size[1]+10)
            pg.display.update(m.rect)

            if event.type == pg.MOUSEBUTTONDOWN:
                if booléen:
                    if index == 2 or event.type == pg.QUIT:
                        pg.quit()
                    elif index == 0:
                        game_menu = False

        pg.event.clear()
screen.fill((255, 255, 255))
pg.display.flip()
pg.key.set_repeat(20, 30)

while game_exit:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            game_exit = False

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_DOWN:

                player.déplacement(player.move[0], player, screen, sprite_width, sprite_height, y=5)

            elif event.key == pg.K_UP:

                player.déplacement(player.move[1], player, screen, sprite_width, sprite_height, y=-5)

            elif event.key == pg.K_RIGHT:

                player.déplacement(player.move[2], player, screen, sprite_width, sprite_height, x=5)

            elif event.key == pg.K_LEFT:

                player.déplacement(player.move[3], player, screen, sprite_width, sprite_height, x=-5)
        if event.type == pg.MOUSEBUTTONDOWN:

            player.stats["HP"] -= 5

        player.hp_bar(screen)


