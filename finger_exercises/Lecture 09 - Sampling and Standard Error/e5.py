# Question 1: Using random.sample Options: Examples independent in hr1, hr2, or
# Both, or Neither. Answer: Neither Rationale: Heart rate data from the MIT-BIH
# Database is a time series with high autocorrelation. Randomly sampling
# indices does not remove the underlying biological dependency between data
# points in a continuous physiological signal.





# Question 2: Getting a random number between 1 and 1800, 250 times.
# Options: Examples independent in hr1, hr2, or Neither.
# Answer: Neither
# Rationale: Similar to random.sample, picking random indices (with replacement) 
# from a single 15-minute window still yields points that are part of the same 
# stochastic process. The proximity of points in a small dataset (1800 points) 
# ensures they remain statistically dependent.





# Question 3: Starting at the first example and going until the 500th example.
# Options: Examples independent in hr1, hr2, or Neither.
# Answer: Neither
# Rationale: This is a sequential block. In a time series, the value at time t 
# is directly dependent on the value at t-1. This is the most obvious case 
# of non-independence due to the temporal nature of the data.
