import pygame as pg
import random as rd
import manage as ma
import fonctions as fc


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


class Spells:

    def __init__(self):

        self.mage_spells = ma.mage_spells
        self.warlock_spells = ma.warlock_spells
        self.warrior_spells = ma.warrior_spells


class Character(NewSprite):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize, posy=0, posx=0):

        NewSprite.__init__(self, sizex, sizey, posx=0, posy=0, rect_x=0, rect_y=0)

        self.group = fc.group_my_spritesheet(data, sizey, sizex, nb_sprite, sheetsize)
        self.nb_sprite = nb_sprite
        self.x = 0  # variable qui change suivant la touche appuyé, défini le déplacement, de 5 pixel par sprite
        self.y = 0  # gauche droite haut bas ( self.x =5 ou -5 self.y = 5 ou -5 )
        self.posx = posx  # position actuel de mon personnage
        self.posy = posy
        self.sizex = sizex  # largeur du sprite ( du personnage à afficher )
        self.sizey = sizey  # hauteur
        self.dirty_rect = []  # dict de liste de rectangle contenant les positions des
        # rectangles à afficher chaque liste contient 2 rectangles, à chaque déplacement le premier et supprimer
        # un nouveau est affiché
        self.hero = fc.load_hero()  # récupération des données de mon champion (seulement les données nécessaire)
        desc = ma.panel[self.hero["Level"]-1]  # -1 à cause du décalage création d'un panel en fonction du niveau de mon
        # personnage
        self.stats = {"HP": desc["HP"][self.hero["Classes"]], "MP": desc["MP"][self.hero["Classes"]],  # je vais
                      "Armor": desc["Armor"][self.hero["Classes"]]}  # chercher les données suivant le rôle ( Classes )
        self.hp_bar = pg.Rect(self.x, self.y-10, int((self.stats["HP"] / desc["HP"][self.hero["Classes"]]) * 30), 6)
        # défini un rectangle pour ma barre de vie (HP actuelle / HP de mon Char full HP * taille du rectangle en pixel)
        self.index = 0
        self.key = pg.key

    def update_character(self, screen, color, i):
        """Update_character permet le déplacement de notre personnage screen = la fenêtre où on affiche
           color = la couleur qu'on veut afficher et index = l'index à récupérer dans notre groupe"""

        self.dirty_rect.append(self.rect)  # On ajoute les nouveaux rectangle
        self.dirty_rect.append(self.hp_bar)
        print(len(self.rect))
        print(self.dirty_rect)
        screen.fill(color)

        sprite = self.group[i][self.index]

        self.posx += self.x  # on ajoute à la position actuelle le déplacement
        self.posy += self.y

        self.rect = pg.Rect(self.posx, self.posy, self.sizex, self.sizey)  # Déplacement du rectangle
        self.hp_bar = pg.Rect(self.posx, self.posy-10, int((self.stats["HP"] /
                                                            ma.panel[self.hero["Level"]-1]["HP"]
                                                            [self.hero["Classes"]]) * 30), 6)

        screen.blit(sprite.image, self.rect)  # on affiche l'image de notre sprite sur la position du rectangle
        pg.draw.rect(screen, (255, 0, 0), self.hp_bar)  # on dessine notre bar de vie
        print(self.rect)
        self.dirty_rect.append(self.rect)  # on ajoute les rectangles afficher à nos liste
        self.dirty_rect.append(self.hp_bar)

        if self.index == self.nb_sprite-1:
            self.index = 0
        else:
            self.index += 1

        self.x = 0  # On remets nos déplacement à 0
        self.y = 0


class Player(Character):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize):

        Character.__init__(self, data, sizex, sizey, nb_sprite, sheetsize, posx=0, posy=0)


class Enemy(Character):

    def __init__(self, data, sizex, sizey, nb_sprite, sheetsize, posy=0):

        Character.__init__(self, data, sizex, sizey, nb_sprite, sheetsize,  posy, posx=0)
        self.hero["Classes"] = "Monster"
        desc = ma.panel[self.hero["Level"]-1]  # Mise à jour des attributs, nouveau panale car il s'est initialisé avec
        self.stats = {"HP": desc["HP"][self.hero["Classes"]], "MP": desc["MP"][self.hero["Classes"]],  # un autre rôle
                      "Armor": desc["Armor"][self.hero["Classes"]]}
