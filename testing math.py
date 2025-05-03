import  random
from game_info import *
luck = 0.9

for i in range(10):
    val = random.random()
    print(val, val <= luck)

inf = GameStats()

print(not inf.armor['HELMET']['equipped'])