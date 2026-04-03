
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here

    #Im my solution i started thinking about using 2 bits for
    #each item so i could use bit masks just like the example
    # and i could also apply a cool unvalid bits verification with
    # O(1) time but it would require 2**(2*M) iterations
    # maybe a better way is possible
    N = len(items)
    
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        tmp = i
        for j in range(N):
            s = tmp % 3;
            tmp //= 3;

            #Three states for each item: 0, 1, 2, out, in bag1, in bag2
            if s == 1:
                combo1.append(items[j])
            if s == 2:
                combo2.append(items[j])


    
        yield combo1, combo2
