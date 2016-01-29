import random as rd
import math


def damage_reduction(armor, damage):

    reduction = (math.log(pow(armor, 5)))
    temp = damage * (reduction / 100)
    damage = int(damage-temp)

    return damage


class Player:
    """Players' attribute and methods"""

    def __init__(self, pseudo):

        self.pseudo = pseudo
        self.level = 1
        self.EXP = 0
        self.inventory = []
        self.HP = 100
        self.MP = 50
        self.gear = {"Helmet": Helmet("", int(), int()), "Shoulders": Shoulders("", int(), int()),
                     "Leggings": Leggings("", int(), int()), "Gloves": Gloves("", int(), int()),
                     "Boots": Boots("", int(), int()), "Weapon": Weapon("", int())}
        self.armor = self.gear["Helmet"].armor+self.gear["Shoulders"].armor+self.gear["Leggings"].armor+\
                     self.gear["Gloves"].armor+self.gear["Boots"].armor

    def attack(self, enemy_life, armor):

        damage = rd.randrange(self.gear["Weapon"].damage-1, self.gear["Weapon"].damage+1, 1)
        damage = damage_reduction(armor, damage)
        enemy_life -= damage
        return enemy_life


class Weapon:

    def __init__(self, name, damage):

        self.name = name
        self.damage = damage


class Gear:

    def __init__(self, name, armor, hp_bonus):

        self.name = name
        self.armor = armor
        self.HP_bonus = hp_bonus


class Helmet(Gear):

    def __init__(self, name, armor, hp_bonus):

        Gear.__init__(self, name, armor, hp_bonus)


class Shoulders(Gear):

    def __init__(self, name, armor, hp_bonus):

        Gear.__init__(self, name, armor, hp_bonus)


class Leggings(Gear):

    def __init__(self, name, armor, hp_bonus):

        Gear.__init__(self, name, armor, hp_bonus)


class Gloves(Gear):

    def __init__(self, name, armor, hp_bonus):

        Gear.__init__(self, name, armor, hp_bonus)


class Boots(Gear):

    def __init__(self, name, armor, hp_bonus):

        Gear.__init__(self, name, armor, hp_bonus)


class Spells:

    def __init__(self):

        self.damage = 0
        self.all_spells_type = {"Fire": Fire}
        self.all_spells_level = {"Fire": Fire.fire_spells_level}


class Fire(Spells, Player):

    def __init__(self):

        Spells.__init__(self)
        self.fire_spells = {"Fireball": self.fire_ball(int(), int())}
        self.fire_spells_level = {"Fireball": 2}

    def fire_ball(self, hp_enemy, armor):

        print(" Fireball !")
        self.damage = rd.randrange(15, 25+self.level, 1)
        self.damage = damage_reduction(armor, self.damage)
        print("{} damage dealt !".format(self.damage))
        hp_enemy -= self.damage
        self.MP -= 10

        return hp_enemy


class Mage(Fire):

    def __init__(self, pseudo):

        Player.__init__(self, pseudo)

    def __str__(self):

        return "Your name is {}, you are level {}, you've got {} HP and {} MP.".format(self.pseudo, self.level, self.HP,
                                                                                       self.MP)


class Enemy:

    def __init__(self):

        self.name = "Grobulus"
        self.HP = 50
        self.armor = 10
        self.xp_reward = 50

    def attack(self, hp_target, armor):

        damage = rd.randrange(8, 13, 1)
        damage = damage_reduction(armor, damage)
        print("{} damage dealt !".format(damage))
        hp_target -= damage

        return hp_target



