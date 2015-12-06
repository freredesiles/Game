import random as rd
import pickle

def mothasard(path_listmots="mots.txt"):
    """
    DESCRIPTION
        Return a word randomly from a dictionnary
    INPUT
        File Path
    """
    with open(path_listmots, "r") as mots:
        listedemots = mots.read()

    listedemots = listedemots.split("\n")
    hasard = rd.randrange(0, len(listedemots))
    mot = listedemots[hasard]

    return mot


def TestMot(mot1, motmyst):

    vie = 8

    while "".join(mot1) != motmyst:
        print("".join(mot1))
        print(motmyst)
        test = False
        temp = "abc"
        while len(temp) > 1:
            temp = input("Saisir une lettre : ")

        for i in range(0, len(mot1)):

            if temp == motmyst[i]:
                mot1[i] = temp
                test = True

        if test is False:
            vie -= 1

        print("".join(mot1))

        print("Il vous reste : "+str(vie)+" !")

        if vie == 0:

            print("Plus de vie !")
            break

    return vie


def PicklePrendreScore(nomjoueur):
    """
    DESCRIPTION
        Take the score of the player
    INPUT
        nomdujoueur: User name
    """
    filename = "score.p"
    
    if not nomjoueur:
        try:
            print "Here are the registered player and their respective score:"
            toutscore =  pickle.load( open( filename, "rb" ) )
            return toutscore
        except IOError:
            print "Their is no registred player yet"
    
    # load the pickle
    try:
        toutscore = pickle.load( open( filename, "rb" ) )
    except IOError:
        print("Their is no score file, I create one ... I create one !  :) ")
        pickle.dump( {}, open( filename, "wb" ) ) # save an empty dictionnary
        toutscore = pickle.load( open( filename, "rb" ) )

    # Take the score
    try:
        return toutscore[nomjoueur]

    except KeyError:
        print("Ton pseudo n'est pas dans la base de donnee")
        toutscore[nomjoueur] = 0
        pickle.dump( toutscore, open( filename, "wb" ) )
        


def StockerScore(nomjoueur, score):
    """
    DESCRIPTION
        Stock the score of the player in the Pickl
    """
    filename = "score.p"
    stockscore = pickle.load(open(filename, "rb" ))
    stockscore[nomjoueur] = score
    pickle.dump(stockscore, open(filename, "wb" ) )
    print "new score saved"
