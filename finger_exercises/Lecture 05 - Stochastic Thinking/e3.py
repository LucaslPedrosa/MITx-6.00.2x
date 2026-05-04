# Write a deterministic program, deterministicNumber, that returns an even
# number between 9 and 21.
#

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 10


# Write a uniformly distributed stochastic program, stochasticNumber, that
# returns an even number between 9 and 21.

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    veryRandom = [10,12,14,16,18,20]
    return random.choice(veryRandom)
