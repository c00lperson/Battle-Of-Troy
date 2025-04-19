import  random
luck = 0.9

for i in range(10):
    val = random.random()
    print(val, val <= luck)