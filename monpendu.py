"""
DESCRIPTION
    This program create the "pendu" game 
    where the user have to guess a word
    in a restricted amount of words
"""

# Import libraries
import Fonctions as fc

mot = []
motmystere = fc.mothasard()

print("Bienvenue dans le jeu du pendu")
print fc.PicklePrendreScore(False)
nomjoueur = input(" Quel est votre pseudo : ")
  
ancienscore = fc.PicklePrendreScore(nomjoueur)

mot = list("*" * len(motmystere))
    
score = fc.TestMot(mot, motmystere)
print("Tu as fais ", str(score), " points")
score += ancienscore
print("Ton score total est de ", str(score), " points")
     
fc.StockerScore(nomjoueur, score)
