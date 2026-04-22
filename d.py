
def gen(dice, e, s=1):
    for i in range(s,e):
        dice.append(i)


dice1 = []
dice2 = []
dice3 = []

gen(dice1, 11)
gen(dice2, 11)
# gen(dice3, 8)

value = 0



for x in dice1:
    for y in dice2:
        # for z in dice3:
        #     if x == y and y == z:
        #         value += 1;
        if x > y:
            value += 1

print(value)


