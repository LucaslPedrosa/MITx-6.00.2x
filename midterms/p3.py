def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """

    n = len(L)
    
    total_sum = 0
    
    multSum = 0

    for element in L:
        thisMult = 0
        for i in range(s+1):
            if (i*element + total_sum <= s):
                thisMult = i
            else:
                break
        total_sum += thisMult*element
        multSum += thisMult

    if total_sum != s:
        return "no solution"
    return multSum


        
lista = [10,9,8,1]
print(greedySum(lista,20))
