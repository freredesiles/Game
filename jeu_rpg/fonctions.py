import pickle as pk
from Game.jeu_rpg import manage as ma


def save(level, pseudo, classe, gear, inventory):

    dic = {"Level": level, "Pseudo": pseudo, "Classe": classe, "Gear": gear, "Inventory": inventory}
    with open("Hero_save", "wb") as save_it:

        saved = pk.Pickler(save_it)
        saved.dump(dic)


def load_hero():

    with open("Hero_save", "rb") as load_it:

        loading = pk.Unpickler(load_it)
        load = loading.load()

    return load


def new_character():

    print("Which classes you want to play?")
    dict_classes = {}
    for index, classes in enumerate(ma.dataframe_hero.index.values):
        dict_classes[index] = classes
        print(str(index) + "- " + classes)
    classes_chosen = int(input(" Type the number next to the classes you want to play"))
    pseudo = input("What's your character name ?")
    save(1, pseudo, dict_classes[classes_chosen], None,  None)
    print("Welcome : " + pseudo + " as level 1 " + dict_classes[classes_chosen])






