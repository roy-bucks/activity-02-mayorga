#import the random module
import random

# modifiers value
modifiers = {
    "target": 1,
    "weather": 1,
    "badge": 1,
    "critical": 1, 
    "random": random.uniform(0.85, 1),
    "stab": 1.5, 
    "type": random.uniform(0.25, 0.50),
    "burn": 1,
    'other': 1,
}

# product of all modifiers
sumMod = 1
for x in modifiers: 
    sumMod *= modifiers[x]

level = 90
power = 110
a = 205
d = 188

damage = ((((((2 * level)/5) + 2) * power * (a/5))/50) + 2) * float(sumMod)

# print the damage
print(damage)