import pygame as pg
import random as rd
import manage as ma
import fonctions as fc


class NewSprite(pg.sprite.Sprite):

    def __init__(self, size_x, size_y, posx=0, posy=0, rect_x=0, rect_y=0):

        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(posx, posy, rect_x, rect_y)  # Initialise the rectangle location
        self.image = pg.Surface((size_x, size_y))  # Initialise a rectangle Surface
        self.x = 0  # Variable which change according to the key pressed +- 5 pixel
        self.y = 0
        self.posx = posx  # Current sprite position
        self.posy = posy
        self.sizex = size_x  # Sprite width
        self.sizey = size_y
        self.dirty_rect = []  # List of rectangle to update
        self.index = 0
        self.key = pg.key

    def sprite_from_sheet(self, data, x, y, sprite_wh, sprite_ht):
        sheet = pg.image.load(data).convert_alpha()
        rectangle = pg.Rect(x, y, sprite_wh, sprite_ht)  # Defini le rectangle ou chercher l'image & taille qu'il fait
        sheet.set_clip(rectangle)
        sheet.set_colorkey((255, 255, 255))
        self.image = sheet.subsurface(sheet.get_clip())

    def update_sprite(self, screen, color, nb_sprite, group_sprite, i=0):

        self.dirty_rect.append(self.rect)
        screen.fill(color)
        sprite = group_sprite[i][self.index]  # i = which group of sprite, self.index = current sprite's state
        self.posx += self.x
        self.posy += self.y
        self.rect = pg.Rect(self.posx, self.posy, self.sizex, self.sizey)
        screen.blit(sprite.image, self.rect)
        self.dirty_rect.append(self.rect)
        pg.display.update(self.dirty_rect)
        self.dirty_rect.clear()
        self.x = 0
        self.y = 0
        if self.index == nb_sprite-1:

            self.index = 0
        else:

            self.index += 1


class Spell(NewSprite):

    def __init__(self, data, size_x, size_y, nb_sprite, sheetsize):
        NewSprite.__init__(self, size_x, size_y)
        self.group_sprite = fc.group_my_spritesheet(data, size_y, size_x, nb_sprite, sheetsize)
        self.nb_sprite = nb_sprite


class Contenu:

    def __init__(self, text, font_size, font_color, screen_size, y=0):

        self.font_size = font_size
        self.font = pg.font.Font(None, self.font_size)
        self.text = text
        self.font_color = font_color
        self.size = self.font.size(self.text)
        self.x = (screen_size[0] - self.size[0])/2
        self.y = (screen_size[1] - self.size[1])/2 + y
        self.text_render = self.font.render(text, 1, font_color)
        self.rectt = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.curseur_in = False

    def collision(self, mouse_x, mouse_y, event):

        if event.type == pg.MOUSEMOTION:
            if self.rectt.collidepoint(mouse_x, mouse_y):
                
                self.curseur_in = True
            else:

                self.curseur_in = False

    def surbrillance(self):

        if self.curseur_in:

            self.font = pg.font.Font(None, self.font_size+5)
            self.text_render = self.font.render(self.text, 1, (155, 155, 155))
            return True
        else:

            self.font = pg.font.Font(None, self.font_size)
            self.text_render = self.font.render(self.text, 1, (255, 255, 255))
            return False


class Character(NewSprite):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize):

        NewSprite.__init__(self, sizex, sizey)
        self.group_sprite = fc.group_my_spritesheet(data, sizey, sizex, nb_sprite, sheetsize)
        self.nb_sprite = nb_sprite
        self.hero = fc.load_hero()  # recover champion 's data
        self.desc = ma.panel[self.hero["Level"]-1]  # -1 because of a shift in the panel
        self.stats = {"HP": self.desc["HP"][self.hero["Classes"]], "MP": self.desc["MP"][self.hero["Classes"]],
                      "Armor": self.desc["Armor"][self.hero["Classes"]]}  # fetch data according to the champion's role
        self.hp_bar = pg.Rect(self.posx, self.posy-10, int((self.stats["HP"] / self.desc["HP"][self.hero["Classes"]]) *
                                                           30), 6)
        # create a rectangle for the character's HP (( current HP / FULL HP) * SIZE_IN_PIXEL)

    def update_character(self, screen, color, i=0):

        self.dirty_rect.append(self.hp_bar)
        self.update_sprite(screen, color, self.nb_sprite, self.group_sprite, i)  # Call to update the character'sprite
        self.hp_bar = pg.Rect(self.posx, self.posy-10, int((self.stats["HP"] / self.desc["HP"][self.hero["Classes"]]) * 30), 6)
        pg.draw.rect(screen, (255, 0, 0), self.hp_bar)  # Draw : (Where, Color, What)
        self.dirty_rect.append(self.hp_bar)
        pg.display.update(self.dirty_rect)
        self.dirty_rect.clear()
        pg.event.clear()


class Player(Character):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize):

        Character.__init__(self, data, sizex, sizey, nb_sprite, sheetsize)
        self.spells_available = fc.spells_available(self.hero["Classes"], self.hero["Level"])  # Input : player's role
        # and player's level, output : Dictionary {"SPELL' S NAME": SPELLSNAME   LEVEL    DAMAGE}

    def cast_spell(self, spell, screen):

        spell.update_sprite(screen, (255, 255, 255), spell.nb_sprite, spell.group_sprite)


class Enemy(Character):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize, posy=0):

        Character.__init__(self, data, sizex, sizey, nb_sprite, sheetsize)
        self.hero["Classes"] = "Monster"
        desc = ma.panel[self.hero["Level"]-1]  # Update attribut for the monster
        self.stats = {"HP": desc["HP"][self.hero["Classes"]], "MP": desc["MP"][self.hero["Classes"]],
                      "Armor": desc["Armor"][self.hero["Classes"]]}
