import random as rd
from Game.jeu_rpg import manage as ma
from Game.jeu_rpg import fonctions as fc


class Spells:

    def __init__(self):

        self.mage_spells = {"Fireball": [3, 4]}  # (level, damage)
        self.warlock_spells = {"Chaosshot": [2, 5]}
        self.warrior_spells = {"Strike": [3, 6]}


class Hero(Spells):

    def __init__(self):

        Spells.__init__(self)
        self.hero = fc.load_hero()
        desc = ma.panel[self.hero["Level"]-1]
        self.stats = {"HP": desc["HP"][self.hero["Classe"]], "MP": desc["MP"][self.hero["Classe"]],
                      "Armor": desc["Armor"][self.hero["Classe"]]}
        self.classe = {"Mage": self.mage_spells, "Warlock": self.warlock_spells, "Warrior": self.warrior_spells}
        self.spells_usable = Hero.spells_available(self)

    def spells_available(self):

        all_spells = self.classe[self.hero["Classe"]]
        spells_usable = {}
        for index, spells in enumerate(all_spells.keys()):

            if self.hero["Level"] >= all_spells[spells][0]:

                spells_usable[index] = spells

        return spells_usable

    def attack(self, spell_name, enemy1):

        damage = self.classe[self.hero["Classe"]][spell_name][1]
        damage = rd.randrange(damage - int(damage*0.2), damage + int(damage*0.2), 1)
        print("{} damage dealt !".format(damage))
        enemy1.defence(damage)

    def defence(self, damage):

        self.stats["HP"] -= damage

    def __str__(self):

        return"{}".format(self.hero)









