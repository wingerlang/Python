#!/usr/bin/env python
#coding: cp1252
import urllib.request, operator, re, sys, time
from operator import itemgetter
import parse_combat as P

def get(url):
	return str(urllib.request.urlopen(url).read())

start, stop = 1, 80
sleepTime = 3
name = "Barnet Rosenbom "
url = "http://g1.setrak.se/char/" + name.lower().replace(" ", "_") + "/log?combat&page="

baseurl = "http://g1.setrak.se"
regex = "/combat/[\d]+"
fightpage, combatlinks = [], [];

for current in range(start, stop+1):
	current_url = url + str(current)
	page = get(current_url)
	fightpage.append(page)
	combatlinks.append(re.findall(regex, page))


total_fights, times_won, times_lost, damage_dealt, damage_received = 0, 0, 0, 0, 0
enemies = {}

#print(combatlinks)
for current_page in range(0, len(combatlinks)):
	print("Page", current_page+1)
	for current_combat in range(0, len(combatlinks[current_page])):
		total_fights += 1
		combat_url = (baseurl + combatlinks[current_page][current_combat])
		winner = (P.battlewinner(get(combat_url)))
		print(combat_url, winner)
		if name in winner[0]:
			times_won += 1
		else:
			if winner[0] in enemies.keys():
				enemies[winner[0]] += 1
			else:
				enemies.update({winner[0]:1})

			times_lost += 1
	print("Time to sleep, %d seconds" % (sleepTime))
	time.sleep(sleepTime)


win_percent = 100 * (times_won / total_fights)
lose_percent = 100 * (times_lost / total_fights)

print("Total fights:", total_fights)
print("Total won:", times_won)
print("Total lost:", times_lost)
print("Win/lose percent %d/%d" % (win_percent, lose_percent))

enemies_sorted = (sorted(enemies.items(), key=itemgetter(1), reverse=True))

for enemy in range(0, len(enemies_sorted)):
	print(enemies_sorted[enemy])