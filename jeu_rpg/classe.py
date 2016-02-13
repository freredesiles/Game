import random as rd
from Game.jeu_rpg import manage as ma
from Game.jeu_rpg import fonctions as fc


class Spells:

    def __init__(self):

        self.mage_spells = ma.mage_spells
        self.warlock_spells = ma.warlock_spells
        self.warrior_spells = ma.warrior_spells


class Hero(Spells):

    def __init__(self):

        Spells.__init__(self)
        self.hero = fc.load_hero()
        desc = ma.panel[self.hero["Level"]-1]
        self.stats = {"HP": desc["HP"][self.hero["Classes"]], "MP": desc["MP"][self.hero["Classes"]],
                      "Armor": desc["Armor"][self.hero["Classes"]]}
        self.classe = {"Mage": self.mage_spells, "Warlock": self.warlock_spells, "Warrior": self.warrior_spells}
        self.spells_usable = fc.spells_available(self.classe[self.hero["Classes"]], self.hero["Level"])

    def attack(self, spell_name, enemy1):

        damage = self.spells_usable[spell_name]["Damage"].values
        print(type(damage))
        damage = rd.randrange(damage - int(damage*0.2), damage + int(damage*0.2), 1)
        print("{} damage dealt !".format(damage))
        enemy1.defence(damage)

    def defence(self, damage):

        self.stats["HP"] -= damage

    def __str__(self):

        return"{}".format(self.hero)











