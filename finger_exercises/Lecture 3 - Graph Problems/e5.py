# Challenge Problem! This problem is difficult and may stump you, but we
# include it because it is very interesting, especially for those who are more
# mathematically inclined.
#
# Don't worry if you can't get all the math behind it, and don't get
# discouraged. Remember that you do not lose points for trying a problem
# multiple times, nor do you lose points if you hit "Show Answer". If this
# problem has you stumped after you've tried it, feel free to reveal the
# solution and read our explanations.
#
# In the following examples, assume all graphs are undirected. That is, an edge
# from A to B is the same as an edge from B to A and counts as exactly one
# edge.
#
# A clique is an unweighted graph where each node connects to all other nodes.
# We denote the clique with  nodes as KN. Answer the following questions in
# terms of .
#
#
#
# How many edges are in KN?
#
# ans: n*(n-1)/2
#
#
# Consider the new version of DFS. This traverses paths until all non-circular
# paths from the source to the destination have been found, and returns the
# shortest one.
#
# Let A be the source node, and B be the destination in KN. How many paths of
# length 2 exist from A to B?
#
# ans: n-2
#
#
# How many paths of length 3 exist from A to B?
#
# ans: (n-2)*(n-3)
#

