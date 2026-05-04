# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.
#



def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')

    N = len(L)
    sizes = [len(s) for s in L]
    m = sum(sizes) / N
    vsum = sum((t - m) ** 2 for t in sizes)
    return (vsum / N) ** 0.5

