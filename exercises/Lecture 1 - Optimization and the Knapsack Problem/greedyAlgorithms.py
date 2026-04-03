
class Item(object):
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.cost = cost

def greedy(itens, maxCost, keyFunction):
    sortedItens = sorted(itens, key=keyFunction, reverse=True)
    totalCost = 0
    totalValue = 0
    for item in sortedItens:
        if totalCost + item.cost <= maxCost:
            totalCost += item.cost
            totalValue += item.value
    return totalValue


def testGreedy(itens, constraint, keyFunction):
    taken = greedy(itens, constraint, keyFunction)
    print('Total value of items taken =', taken)
    
    return taken


def testGreedys(itens, constraint):
    print('Use greedy by value to allocate', constraint, 'cost')
    testGreedy(itens, constraint, lambda x: x.value)

    print('\nUse greedy by cost to allocate', constraint, 'cost')
    testGreedy(itens, constraint, lambda x: 1 / x.cost)

    print('\nUse greedy by density to allocate', constraint, 'cost')
    testGreedy(itens, constraint, lambda x: x.value / x.cost if x.cost != 0 else float('inf'))

def buildItems(name, value, cost):
    itens = []
    for name, value, cost in zip(name, value, cost):
        itens.append(Item(name, value, cost))

    return itens

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10, 79]
calories = [123, 154, 258, 354, 365, 150, 95, 195, 305]

foods = buildItems(names, values, calories)
testGreedys(foods, 750)


#Note: The greedy algorithm does not always yield the optimal 
# solution for the knapsack problem
# even if it can provide a good approximation in many cases.
