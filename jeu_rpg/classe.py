import random as rd


class Spells:

    def __init__(self):

        self.mage_spells = {"Fireball": (3, 4)}  # (level, damage)
        self.warlock_spells = {"ChaosShot": (2, 5)}
        self.warrior_spells = {"Strike": (3, 6)}


class Hero(Spells):

    def __init__(self, pseudo, classe):

        Spells.__init__(self)
        self.damage = None
        self.HP = 100
        self.pseudo = pseudo
        self.classe_chosen = classe
        self.MP = 50
        self.level = 4
        self.classe = {"Mage": self.mage_spells, "Warlock": self.warlock_spells, "Warrior": self.warrior_spells}
        self.spells_usable = {}

    def spells_available(self):

        for index, spells in enumerate(self.classe[self.classe_chosen].keys()):

            if self.level >= self.classe[self.classe_chosen][spells][0]:

                self.spells_usable[index] = spells

    def attack(self, spell_name, enemy_hp):
        damage = self.classe[self.classe_chosen][spell_name][1]

        self.damage = rd.randrange(damage - (int(2*(damage/10))), damage + (int(2*(damage/10))), 1)

        print("{} damage dealt !".format(self.damage))
        enemy_hp -= self.damage

        return enemy_hp

    def __str__(self):

        return "Pseudo: {}\nclasse: {}\nlevel: {}\nspells usable: {}".format(self.pseudo, self.classe_chosen, self.level
                                                                             , self.spells_usable.values())

player = Hero("Jean", "Mage")
player.spells_available()
print(player)






