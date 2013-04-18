#!/usr/bin/env python
#coding: cp1252
import urllib.request
import re, sys

def battlewinner(string):
	regex_winner = r"</p>[</div>]*<p>" + r'([a-zA-Z0-9,\\\s]+)' + "vinner striden</p>"
	#print(regex_winner)
	return re.findall(regex_winner, string, re.IGNORECASE)

def regexresult(r):
	if r:
		print(r)
	else:
		print("No result")

def removeSomeHTML(s):
	return str(re.sub('<[^>]*>', ' ', s))

def doStuff():
	name = "Barnet Rosenbom"
	hitstring = name + " tr\\xc3\\xa4ffar"

	f = str(urllib.request.urlopen("http://g1.setrak.se/combat/373409").read())
	parsed = " ".join(removeSomeHTML(str((f[f.find("Runda 1"):]))).split())

	print(parsed)
	print(parsed.count(hitstring))
	print("\n")

	regex = name + " tr\\\\xc3\\\\xa4ffar" + r'(.+?)' + r"\(( HP)\)"
	regex2 = " tr\\\\xc3\\\\xa4ffar " + name + r" \((.+?)\)"


	you_hit = re.findall(regex, parsed)
	hit_you = re.findall(regex2, parsed)


	regexresult(you_hit)
	regexresult(hit_you)

	print(battlewinner(f))

#doStuff()