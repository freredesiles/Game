#===============================================================================
# TUTORIALS
#    Gentic algorithm: http://lethain.com/genetic-algorithms-cool-name-damn-simple/
#    Neural netowkr http://lethain.com/genetic-algorithms-cool-name-damn-simple/
#
#    TODO
#        Lorsque un monstre meurt un autre le ramplace initializer 
#        avec les monstres qui on le plus d energie
#        
##===============================================================================

import matplotlib.pyplot as plt


import numpy as np
from gtk.keysyms import equal

#===============================================================================
# Activation function
#===============================================================================
def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0 - np.tanh(x)**2

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))

#===============================================================================
# Neural Network
#=============================================================================== 
class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        """
        :param layers: A list containing the number of units in each layer.
        Should be at least two values
        :param activation: The activation function to be used. Can be
        "logistic" or "tanh"
        """
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2*np.random.random((layers[i - 1] + 1, layers[i]
                                + 1))-1)*0.25)
        self.weights.append((2*np.random.random((layers[i] + 1, layers[i +
                            1]))-1)*0.25)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1] = x
        output = temp
        for l in range(0, len(self.weights)):
            output = self.activation(np.dot(output, self.weights[l]))
        return output
     
input_neurons = 2
hidden_neurons = 2
output_neurons = 2
activ_methods =  'tanh'

nn = NeuralNetwork([input_neurons, hidden_neurons, output_neurons], 'tanh') # 2 input, 2 hidden neurons and 2 outputs
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0,1], [1,1], [1,0], [1, 0]])
# nn.fit(X, y)
for i in X:
    print(i,nn.predict(i))


class monster():
    def __init__(self,layers, activ_methods):
        self.energy = 1 
        self. position = []
        self.nn = NeuralNetwork(layers, activ_methods)
    def eyes(self):
        """
        Take the state of the array in the environnement surronding the monster
        """
        x, y = self.position
        left = self.position[x-1, y] 
        right = self.position[x+1, y]
        front = self.position[x, y+1]
        back = self.position[x, y-1]
        return [right, left, front, back]

    def move(self):
        """
        Take the input from eyes
        and move on the environnemnent base on the output of the nn
        """
        vision = self.eyes
        for v in vision:
            move_monster = nn.predict(v)
        self.position = move_monster
    
        
    

#===============================================================================
# Create an environnement
# Create a population of monster
#===============================================================================
from random import randint

class Env():
    """
    The environnement
    """
    def __init__(self, len_x, len_y):
        self.len_x = len_x
        self.len_y =len_y
        self.env = np.zeros((len_x, len_y)) # environnemnt with value to polot
        self.env_monster = np.empty((len_x, len_y), dtype=object) # environnement with the monster objects

    def spawn(self, object, position=None, rand= False):
        """
        poisition: list, [x,y] position of the object to be put in the env
        """
        for ob in object:
            if rand:
                pos_x = np.random.randint(0, self.len_x)
                pos_y = np.random.randint(0, self.len_y)
                self.env[pos_x, pos_y] = ob
            else:
                self.env[position[0], position[1]] = ob
    def set_food(self, food):
        """
        food: a list of energy object
        """
        env_food = self.spawn(food, rand =True)
        print "Food -- "*10
        print "Food set_up!"

    def set_monster(self, count,layers, activ_methods ):
        """
        Initialize the pouplation of monsters
        """
        self.pop = {}
        for i in range(count):
            pos_x = np.random.randint(0, self.len_x)
            pos_y = np.random.randint(0, self.len_y)
            nn = monster(layers, activ_methods)
            nn.position = [pos_x, pos_y]
            self.env_monster[pos_x, pos_y] = nn
            self.env[pos_x, pos_y] = 1
            self.pop["net_"+str(i)] = nn

    
    def get_pool_weight(self):
        pool = []
        for m in self.pop:
            pool.append(self.pop[m].nn.weights)
        return pool     
    def run(self, epochs):
        """
        Run the program for the number of epochs
        """
        rate_energy_loss = 0.1 # The rate at which the monster loose energy at every epochs 
        pop = self.pop
        epoch = 0 
        while epoch <= epochs and len(pop.keys())>0:
            print "*"*100
            print "EPOCHS" + str(epoch)
            for m in pop.keys():
                # check the state of every monster
                if pop[m].energy>0:
                    pop[m].energy = pop[m].energy -rate_energy_loss # use energy
                else:
                    del pop[m]
            print "Their is " + str(len(pop.keys())) + " Monster alive!"
            self.pop = pop
            epoch +=1
        print "The universe is over ... "
        print "It ended with "+ str(len(pop.keys()))+ " Monster alive!"
        
    
    
def Main():
    """
    Run the main program
    """
    
    len_x = 200
    len_y = 200
    
    food = [1]*10
    
    activ_methods =  'tanh'
    count = 100
    input_neurons = 4
    hidden_neurons = 2
    output_neurons = 2
    layers = [input_neurons,hidden_neurons,output_neurons,]
    
    env = Env(len_x, len_y)
    env.set_food(food)
    env.set_monster(count, layers, activ_methods)
#     pool = env.get_pool_weight()
    env.run(100)

if __name__=='__main__':
    Main()

#===========================================================================
# Genetic algorithm
#===========================================================================
# 
# 
# 
# # We don't need the fitness function
# from operator import add
# def fitness(individual, target):
#     """
#     Determine the fitness of an individual. Lower is better.
#     individual: the individual to evaluate
#     target: the sum of numbers that individuals are aiming for
#     """
#     summation = reduce(add, individual, 0)
#     return abs(target-summation)
# 
# x = individual(5,0,100)
# fitness(x, 200)
#  
# def grade(pop, target):
#     'Find average fitness for a population.'
#     summed = reduce(add, (fitness(x, target) for x in pop), 0)
#     return summed / (len(pop) * 1.0)
# 
# 
# father = [1,2,3,4,5,6]
# mother = [10,20,30,40,50,60]
# child = father[:3] + mother[3:]
# child
# 
# pop = population(3,5,0,100)
# 
# from random import random, randint
# chance_to_mutate = 0.01
# for i in pop:
#     if chance_to_mutate > random():
#         place_to_modify = randint(0,len(i))
#         i[place_to_modify] = randint(min(i), max(i))

