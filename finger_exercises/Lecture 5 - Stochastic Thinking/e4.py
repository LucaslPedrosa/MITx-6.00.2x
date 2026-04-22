# Are the following two distributions equivalent?

import random
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

# Ans: Yes
#
#


# Are the following two distributions equivalent?

import random
def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

# Ans: Yes


# Are the following two distributions equivalent?

import random
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)

# Ans: No, dist6 can return 10, while dist5 can only return up to 9.
