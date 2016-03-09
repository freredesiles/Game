import pygame as pg
import random as rd
import Game.BIGPROJECTRPG.manage as ma
import Game.BIGPROJECTRPG.fonctions as fc


def group_my_spritesheet(data, sprite_height, sprite_width, nb_sprite, sheet_size):
    list_group_sprite = []

    for line in range(0, sheet_size, sprite_height):
        groupe = pg.sprite.OrderedUpdates()

        for sprite_lenght in range(0, (sprite_width*nb_sprite), sprite_width):

            sprite_load = NewSprite(sprite_width, sprite_height)
            sprite_load.sprite_from_sheet(data, sprite_lenght, line, sprite_width, sprite_height)
            groupe.add(sprite_load)

        list_group_sprite.append(groupe)

    return list_group_sprite


class NewSprite(pg.sprite.Sprite):

    def __init__(self, size_x, size_y, posx=0, posy=0, rect_x=0, rect_y=0):

        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(posx, posy, rect_x, rect_y)  # Defini le rectangle ou positionner l'image
        self.image = pg.Surface((size_x, size_y))  # Créer une surface rectangulaire

    def sprite_from_sheet(self, data, x, y, sprite_wh, sprite_ht):

        sheet = pg.image.load(data).convert()
        rectangle = pg.Rect(x, y, sprite_wh, sprite_ht)  # Defini le rectangle ou chercher l'image & taille qu'il fait
        sheet.set_clip(rectangle)
        sheet.set_colorkey((255, 255, 255))
        self.image = sheet.subsurface(sheet.get_clip())


class Contenu:

    def __init__(self, text, font_size, font_color, screen_size, y=0):

        self.font_size = font_size
        self.font = pg.font.Font(None, font_size)
        self.text = text
        self.font_color = font_color
        self.size = self.font.size(self.text)
        self.x = (screen_size[0] - self.size[0])/2
        self.y = (screen_size[1] - self.size[1])/2 + y
        self.text_render = self.font.render(text, 1, font_color)
        self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
        self.curseur_in = False

    def collision(self, mouse_x, mouse_y, event):

        if event.type == pg.MOUSEMOTION:
            if self.rect.collidepoint(mouse_x, mouse_y):
                
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


class Spells:

    def __init__(self):

        self.mage_spells = ma.mage_spells
        self.warlock_spells = ma.warlock_spells
        self.warrior_spells = ma.warrior_spells


class Personnage(Spells):

    def __init__(self, data, spritewidth, spriteheight, nb_sprite, sheet_size, x=0, y=0):

        Spells.__init__(self)
        self.move = group_my_spritesheet(data, spritewidth, spriteheight, nb_sprite, sheet_size)
        self.x = x
        self.y = y
        self.hero = fc.load_hero()
        desc = ma.panel[self.hero["Level"]-1]
        self.stats = {"HP": desc["HP"][self.hero["Classes"]], "MP": desc["MP"][self.hero["Classes"]],
                      "Armor": desc["Armor"][self.hero["Classes"]]}
        self.classe = {"Mage": self.mage_spells, "Warlock": self.warlock_spells, "Warrior": self.warrior_spells}
        self.spells_usable = fc.spells_available(self.classe[self.hero["Classes"]], self.hero["Level"])

    def déplacement(self, groupe_dep, player, screen, sprite_witdh, sprite_height, x=0, y=0):

        for sprite in groupe_dep:

            player.x += x
            player.y += y
            screen.fill((255, 255, 255))
            screen.blit(sprite.image, [player.x, player.y, sprite_witdh, sprite_height])
            player.hp_bar(screen, x, y)
            sprite.rect = fc.update_sprite(player.x, player.y, sprite_witdh, sprite_height, x, y)
            pg.display.update(sprite)
            pg.time.delay(20)

    def create_enemy(self, hero_level):

        del(self.hero, self.classe)

        if hero_level <= 3:

            level = rd.randrange(hero_level - 2, hero_level + 1)

        else:

            level = hero_level

        hp = rd.randrange(80 + 0.2 * level * 10, 110 + 0.2 * level * 10)
        mp = rd.randrange(30 + 0.2 * level * 10, 60 + 0.2 * level * 10)
        armor = rd.randrange(20 + 0.2 * level * 10, 30 + 0.2 * level * 10)
        self.stats = {"Level": level, "Pseudo": rd.choice(ma.list_name), "HP": hp, "MP": mp, "Armor": armor}

    def attack(self, spell_name, enemy1):

        damage = self.spells_usable[spell_name]["Damage"].values
        print(type(damage))
        damage = rd.randrange(damage - int(damage*0.2), damage + int(damage*0.2), 1)
        print("{} damage dealt !".format(damage))
        enemy1.defence(damage)

    def defence(self, damage):

        self.stats["HP"] -= damage

    def hp_bar(self, screen, dx=0, dy=0):

        desc = ma.panel[self.hero["Level"]-1]
        taille_rect_x = int((self.stats["HP"] / desc["HP"][self.hero["Classes"]]) * 30)
        rect = pg.Rect(self.x, self.y-10, taille_rect_x, 6)
        pg.draw.rect(screen, (255, 0, 0), rect)
        rect = fc.update_sprite(self.x, self.y-10, taille_rect_x, 6, dx, dy)
        pg.display.update(rect)





