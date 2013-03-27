"""
104% betyder att man är mycket nära att träffa. Över 100% missar man, annars träffar man. 
Mer exakt är det en lottdragning, där det är en lott att träffa för varje poäng den som slår har i träffsäkerhet,
 och en lott att missa för varje poäng den som blir slagen har i undvika. Lotterna är sorterade, och det används 
till att räkna ut avståndet man missar med.
 """
import random

def percent(n):
    return round(n * 100)

def determineHit(hit, avoid, parry = 0):
    total = hit + avoid + parry
    rand = random.randint(0, total-1)
    return percent(rand / hit) 

hit, avoid, parry = 20, 10, 10
numHits, rounds = 0, 100000


for i in range(rounds):
    if determineHit(hit, avoid) < 100:
        if determineHit(hit, parry) < 100:
            numHits += 1

print("Rounds", rounds)
print("numHits", numHits)
print("percent", percent(numHits/rounds))

numHits, rounds = 0, 100000
for i in range(rounds):
    if determineHit(hit, avoid, parry) < 100:
        numHits += 1

print("Rounds", rounds)
print("numHits", numHits)
print("percent", percent(numHits / rounds))