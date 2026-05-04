# You have a bucket with 3 red balls and 3 green balls. Assume that once you
# draw a ball out of the bucket, you don't replace it. What is the probability
# of drawing 3 balls of the same color?
#
# Write a Monte Carlo simulation to solve the above problem. Feel free to write
# a helper function if you wish.

import random



def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    drawn = 0
    # Your code here
    for _ in range(numTrials):
        bucket = ['red', 'red', 'red', 'green', 'green', 'green']
        draw = []
        for i in range(3):
            n = random.randint(0,5-i)
            draw.append(bucket[n])
            bucket.remove(bucket[n])
        
        drawn += (draw[0] == draw[1] == draw[2])
    
    return drawn/numTrials
        


    
    

