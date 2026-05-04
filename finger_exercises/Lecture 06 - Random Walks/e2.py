# Exercise 2
# 2.0/2.0 points (graded)
# 1. Is the following code deterministic or stochastic?



import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)


# Deterministic
#
# Stochastic
#
# Ans: Stochastic, because the number of iterations in the loop is random, and
# the number of times the if statement is true is also random. The seed only
# affects the random numbers generated within each iteration, but it does not
# make the overall behavior of the code deterministic.


# 2. Which of the following alterations (Code Sample A or Code Sample B) would result in a deterministic process?

import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)

    
    
# Code Sample B
mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)




# Check one or both.
#
#
#
# Code Sample A
#
# Code Sample B

# Ans: both Code Sample A and Code Sample B would result in a deterministic
# process. In both samples, the random seed is set to 0 before any random
# numbers are generated, which means that the sequence of random numbers will
# be the same every time the code is run. Therefore, both samples will produce
# the same output each time they

