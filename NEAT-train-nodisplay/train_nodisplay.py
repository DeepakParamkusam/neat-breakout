"""
 neat-python 0.7 by CodeReclaimers <http://codereclaimers.com>

 Implemenation by Deepak, Divyam, Gokul and Vimanyu; TU Delft 2016 
"""

from neat import nn, population, statistics, visualize
import bricka_nodisplay
import pickle

def eval_fitness(genomes):    
    for g in genomes:
        net = nn.create_feed_forward_phenotype(g)
        g.fitness = bricka_nodisplay.Bricka().run(net)/20.0

pop = population.Population('xor2_config')
pop.run(eval_fitness, 300)
#winner = pop.statistics.best_genome()
#winner_net = nn.create_feed_forward_phenotype(winner)

winner = pop.statistics.best_genome()

with open('../NEAT_Verify/trained_models/Try_06_3.pkl', 'wb') as output:
    pickle.dump(winner,output,pickle.HIGHEST_PROTOCOL)
    

