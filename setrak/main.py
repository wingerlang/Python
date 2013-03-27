from fighter import Fighter
from weapon import Weapon
import random
import chars

def percent(n):
    return round(n * 100)

def determineHit(hit, avoid, parry = 0):
    total = hit + avoid + parry
    rand = random.randint(0, total-1)
    return percent(rand / hit) 

def tryToHit(p1, p2):
	p1_hit = p1.getAccuracy()
	p2_avoid = p2.getAvoid()
	p2_parry = p2.getParry()

	hitpercent = determineHit(p1_hit, p2_avoid, p2_parry)
	if hitpercent < 100:
		#print(p1,"HIT", p2.bleed(p1.attack()))
		p2.bleed(p1.attack())
		return True
	else:
		#print(p1,"Miss", hitpercent, "%\n")
		return False

def duel(p1, p2):
	roundNr = 1
	while p1.health() > 0 and p2.health() > 0:
		#print("Round " + str(roundNr))
		tryToHit(p1, p2)
		tryToHit(p2, p1)
		roundNr += 1
		p1.getTired(roundNr)
		p2.getTired(roundNr)
		if roundNr > 75:
			break

	return "p1" if p1.health() > p2.health() else "p2" 

p1stats, p2stats, games = 0, 0, 100000
for i in range(games):
	p1, p2, troll = Fighter(chars.rosenbom2), Fighter(chars.bergsrese), Fighter({})
	winner = duel(p1, p2)
	if winner == 'p2':
		p2stats += 1
	else:
		p1stats += 1

print()
print(p1, "vs", p2)
print(p1stats, '-', p2stats)
print(str(100 * (p1stats/games)) + "%")