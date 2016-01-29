import Game.classe as cl


def check_spells(player_level, spells_level, player_spells):

    spells_usable = {}

    for spells in spells_level.keys():

        if player_level >= spells_level[spells]:

            spells_usable[str(spells)] = player_spells[spells]

    print(" 0- Use your {} !".format(player1.gear["Weapon"].name))

    list_value = []
    index = 1
    for index, value in enumerate(spells_usable):

        list_value.append(value)
        print(" {}- {}".format(index, value))

    return spells_usable, list_value


def attack(enemy_hp, player_hp, spell, enemy_armor, player_armor):

    enemy_hp = spell(enemy_hp, enemy_armor)
    print(enemy_hp)


def combat(enemy_name, enemy_hp, enemy_armor, player_hp, player_armor, spellslvl, allspells):

    print("You are fighting vs {}".format(enemy_name))
    print("You attack first !")
    print("Spells available :")
    spells_usable, spells_available = check_spells(player1.level, spellslvl, allspells)
    spell_use = int(input("What do you want to attack with"))

    if spell_use == 0:
        print("You chose {}".format(player1.gear["Weapon"].name))
    else:
        print("You chose {}".format(spells_usable[spells_available[spell_use-1]]))

    attack(enemy_hp, player_hp, spells_usable[spells_available[spell_use-1]], enemy_armor, player_armor)

player1 = cl.Player("Mon gland frais")
enemy1 = cl.Enemy()
player1.level = 5
all_spells = cl.Spells()
player1.gear["Weapon"] = cl.Weapon("Bigsword", 10)
combat(enemy1.name, enemy1.HP, enemy1.armor, player1.HP, player1.armor, all_spells.spells_level, all_spells.all_spells)
