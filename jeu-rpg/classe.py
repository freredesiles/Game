import random as rd



class Spells:

    def __init__(self):

        self.mage_spells = {"Fireball": (3, 40)}  # (level, damage)
        self.warlock_spells = {"ChaosShot": (2, 5)}
        self.warrior_spells = {"Strike": (3, 6)}


class Hero(Spells):

    def __init__(self, pseudo, clas):

        Spells.__init__(self)

        self.caract = {"HP": 100, "pseudo": pseudo, "Profession": clas, "MP": 50, "level": 1, "armor": 10}
        c = self.caract
        self.classe = {"Mage": (self.mage_spells, c["HP"]-30, c["MP"]+20), "Warlock": (self.warlock_spells, c["HP"]-15,
                                                                                       c["MP"]+20),
                       "Warrior": (self.warrior_spells, c["HP"]+40, c.pop("MP"))}

        self.spells_usable = {}

    def spells_available(self):

        all_spells = self.classe[self.caract["Profession"]]

        for index, spells in enumerate(all_spells.keys()):

            if self.caract["level"] >= all_spells[spells][0]:

                self.spells_usable[index] = spells

    def attack(self, spell_name, enemy1):

        damage = self.classe[self.caract["Profession"]][spell_name][1]
        damage = rd.randrange(damage - int(damage*0.2), damage + int(damage*0.2), 1)
        print("{} damage dealt !".format(damage))
        enemy1.defence(damage)

    def defence(self, damage):

        self.caract["HP"] -= damage

    def __str__(self):

        return"{}".format(self.caract)

player = Hero("Jean", "Warlock")
enemy = Hero("Patrick", "Warlock")

print(player)






