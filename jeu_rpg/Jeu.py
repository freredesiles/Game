from Game.jeu_rpg import classe as cl
from Game.jeu_rpg import fonctions as fc
from Game.jeu_rpg import manage as ma
print("Welcome ! Do you want to create a new character ?")
choice = input("o/n ? ")

if choice == "o":

    fc.new_character(ma.dataframe_hero.index.values)
    player = cl.Hero()

else:

    player = cl.Hero()



