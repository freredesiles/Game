import pandas as pd


dataframe_hero = pd.read_csv("/home/martin/Documents/gitproject/BIGPROJECTRPG/HERO.csv", index_col=[0])
dataframe_temp = pd.read_csv("/home/martin/Documents/gitproject/BIGPROJECTRPG//HERO.csv", index_col=[0])
dataframe_hero.index.rename("Rôle")
panel = pd.Panel.from_dict({0: dataframe_hero})

for i in range(51):

    dataframe_hero["HP"] = 0.06 * dataframe_temp["HP"]+dataframe_temp["HP"]
    dataframe_hero["MP"] = 0.06 * dataframe_temp["MP"] + dataframe_temp["MP"]
    dataframe_hero["Armor"] = 0.06 * dataframe_temp["Armor"] + dataframe_temp["Armor"]
    dataframe_temp = dataframe_hero
    panel[i+1] = dataframe_hero


mage_spells = pd.read_csv("/home/martin/Documents/gitproject/BIGPROJECTRPG/Mage_spells.csv")
warrior_spells = pd.read_csv("/home/martin/Documents/gitproject/BIGPROJECTRPG/Warrior_spells.csv")
warlock_spells = pd.read_csv("/home/martin/Documents/gitproject/BIGPROJECTRPG/Warlock_spells.csv")
