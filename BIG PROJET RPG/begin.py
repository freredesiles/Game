import pygame as pg


def groupe_sprites_sheet_charact(data, y, sprite_size):
    groupe = pg.sprite.OrderedUpdates()
    for sprite_lenght in range(0, (sprite_size*8), sprite_size):
        sprite_load = SpriteSheet(data, x=sprite_lenght, y=y*sprite_size*2)
        groupe.add(sprite_load)
    return groupe


class SpriteSheet(pg.sprite.Sprite):

    def __init__(self, data, x=0, y=0, posx=0, posy=0):
        pg.sprite.Sprite.__init__(self)
        self.sheet = pg.image.load(data).convert()
        self.rect = pg.Rect(posx, posy, 32, 64)  # Defini le rectangle ou positionner l'image
        self.image = SpriteSheet._set_attribute(self, x, y)

    def _set_attribute(self, x, y):
        rectangle = pg.Rect(x, y, 32, 64)  # Defini le rectangle ou chercher l'image et la taille qu'il fait
        self.sheet.set_clip(rectangle)
        self.sheet.set_colorkey((255, 255, 255))
        return self.sheet.subsurface(self.sheet.get_clip())


class Personnage:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def déplacement(self, groupe_dep, x=0, y=0):
        for sprite in groupe_dep:
            player.x += x
            player.y += y
            screen.fill((25, 130, 50))
            screen.blit(sprite.image, [player.x, player.y, 32, 64])
            if y > 0:
                sprite.rect = (player.x, player.y-y, 32, 64+y)
            elif y < 0:
                sprite.rect = (player.x, player.y, 32, 64-y)
            elif x > 0:
                sprite.rect = (player.x-x, player.y, 32+x, 64)
            else:
                sprite.rect = (player.x, player.y, 32-x, 64)
            pg.display.update(sprite)
            pg.time.delay(20)


pg.init()
taille_fenêtre = (800, 500)
screen = pg.display.set_mode(taille_fenêtre)  # Taille de la fenêtre
screen.fill((25, 130, 50))
pg.display.flip()
player = Personnage()
descendre = groupe_sprites_sheet_charact("image/Roman.png", 0, 32)
monter = groupe_sprites_sheet_charact("image/Roman.png", 1, 32)
droite = groupe_sprites_sheet_charact("image/Roman.png", 2, 32)
gauche = groupe_sprites_sheet_charact("image/Roman.png", 3, 32)
game_exit = True
pg.key.set_repeat(20, 5)
while game_exit:
    for event in pg.event.get():

        if event.type == pg.QUIT:

            game_exit = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:

                player.déplacement(descendre, y=5)

            elif event.key == pg.K_UP:

                player.déplacement(monter, y=-5)

            elif event.key == pg.K_LEFT:

                player.déplacement(gauche, x=-5)

            elif event.key == pg.K_RIGHT:

                player.déplacement(droite, x=5)




