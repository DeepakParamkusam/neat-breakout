import pickle
from neat import nn, parallel, population, visualize
from neat.config import Config
from neat.math_util import mean

with open('best.pkl', 'rb') as f:
    winner=pickle.load(f)
print(winner)

#visualize.draw_net(winner, view=True, filename="nn_winner.gv")
#visualize.draw_net(winner, view=True, filename="nn_winner-enabled.gv", show_disabled=False)
visualize.draw_net(winner, view=True, filename="nn_winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)
    
