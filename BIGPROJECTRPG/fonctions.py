import pickle as pk
import pygame as pg
import all_class as ac
import manage as ma


def save(level, pseudo, classe, gear, inventory):

    dic = {"Level": level, "Pseudo": pseudo, "Classes": classe, "Gear": gear, "Inventory": inventory}
    with open("/home/martin/Documents/gitproject/BIGPROJECTRPG/Hero_save", "wb") as save_it:

        saved = pk.Pickler(save_it)
        saved.dump(dic)


def load_hero():

    with open("/home/martin/Documents/gitproject/BIGPROJECTRPG/Hero_save", "rb") as load_it:

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


def spells_available(role, hero_level):
    spells_usable = {}
    if role == "Mage":
        df_spells = ma.mage_spells
    elif role == "Warrior":
        df_spells = ma.warrior_spells
    else:
        df_spells = ma.warlock_spells

    for index in range(len(df_spells)):

        if df_spells["Level"][index] <= hero_level:

            spells_usable[df_spells["Spells"][index]] = df_spells[index:index+1]

    return spells_usable


def group_my_spritesheet(data, sprite_height, sprite_width, nb_sprite, sheet_height):

    list_group_sprite = []

    for line in range(0, sheet_height, sprite_height):
        groupe = []

        for sprite_lenght in range(0, (sprite_width*nb_sprite), sprite_width):

            sprite_load = ac.NewSprite(sprite_width, sprite_height)
            sprite_load.sprite_from_sheet(data, sprite_lenght, line, sprite_width, sprite_height)
            groupe.append(sprite_load)

        list_group_sprite.append(groupe)

    return list_group_sprite


def outbound(screen_x, screen_y, posx, posy, sprite_x, sprite_y):

    if posx > screen_x or posx < 0-sprite_x or posy > screen_y or posy < 0-sprite_y:

        return True

    return False


def erase_rect(screen, color, rect):

    screen.fill(color)
    pg.display.update(rect)


def check_alive(sprite_list, screen, background):

    for sprite in sprite_list:

        if issubclass(type(sprite), ac.Character):
            if not sprite.alive:
                erase_rect(screen, background, sprite.rect)
                sprite_list.remove(sprite)

    return sprite_list


def update_sprite(list_sprite_screen, screen, background, index):

    if len(list_sprite_screen) is not 0:
        for sprite in list_sprite_screen:
            if isinstance(sprite, ac.Player):
                sprite.update_character(screen, background, index)

            elif isinstance(sprite, ac.Spell):

                sprite.update_spell(screen, background)

            elif isinstance(sprite, ac.Enemy):

                sprite.update_character(screen, background, 0)


def sprite_collision(list_sprite_screen, screen, background):

    new_sprite_liste = list_sprite_screen[:]

    if len(list_sprite_screen) is not 0:
        for i, sprite1 in enumerate(list_sprite_screen):
            for j, sprite2 in enumerate(list_sprite_screen):
                if j > i:

                    collision = pg.Rect.colliderect(sprite1.rect, sprite2.rect)

                    if collision:

                        new_sprite_liste = filtre(sprite1, sprite2, screen, background, list_sprite_screen)

    return new_sprite_liste


def filtre(sprite1, sprite2, screen, background, list_sprite_screen):

    if issubclass(type(sprite1), ac.Character):

        list_sprite_screen = collision_with(sprite1, sprite2, list_sprite_screen, screen, background)

    elif issubclass(type(sprite2), ac.Character):

        list_sprite_screen = collision_with(sprite2, sprite1, list_sprite_screen, screen, background)

    return list_sprite_screen


def collision_with(sprite_char, sprite, list_sprite_screen, screen, background):

    if type(sprite) == ac.Spell and sprite.who_cast is not sprite_char:

        sprite_char.defence(sprite)
        list_sprite_screen.remove(sprite)
        erase_rect(screen, background, sprite.rect)

    return list_sprite_screen







