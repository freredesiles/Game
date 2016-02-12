import pandas as pd
import os

os.chdir("/home/pierre/Documents/PycharmProjects/Game/jeu_rpg")

dataframe = pd.read_csv("test.csv")

dataframe_temp = pd.read_csv("test.csv")

panel = pd.Panel.from_dict({0: dataframe})

for i in range(51):

    dataframe["Pseudo"] = "Pseudo"
    dataframe["HP"] = 0.06 * dataframe_temp["HP"]+dataframe_temp["HP"]
    dataframe["MP"] = 0.06 * dataframe_temp["MP"] + dataframe_temp["MP"]
    dataframe["Level"] = i
    dataframe["Rôle"] = dataframe_temp["Rôle"]
    dataframe["Armor"] = 0.06 * dataframe_temp["Armor"] + dataframe_temp["Armor"]

    dataframe_temp = dataframe

    panel[i+1] = dataframe

