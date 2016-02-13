import pickle as pk


def save(level, pseudo, classe, gear, inventory):

    dic = {"Level": level, "Pseudo": pseudo, "Classes": classe, "Gear": gear, "Inventory": inventory}
    with open("Hero_save", "wb") as save_it:

        saved = pk.Pickler(save_it)
        saved.dump(dic)


def load_hero():

    with open("Hero_save", "rb") as load_it:

        loading = pk.Unpickler(load_it)
        load = loading.load()

    return load


def new_character(all_classes):

    print("Which classes you want to play?")
    dict_classes = {}
    for index, classes in enumerate(all_classes):
        dict_classes[index] = classes
        print(str(index) + "- " + classes)
    classes_chosen = int(input(" Type the number next to the classes you want to play"))
    pseudo = input("What's your character name ?")
    save(2, pseudo, dict_classes[classes_chosen], None,  None)
    print("Welcome : " + pseudo + " as level 1 " + dict_classes[classes_chosen])


def spells_available(df_spells, hero_level):
    spells_usable = {}
    for index in range(len(df_spells)):

        if df_spells["Level"][index] <= hero_level:

            spells_usable[df_spells["Spells"][index]] = df_spells[index:index+1]

    return spells_usable



