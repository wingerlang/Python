import random

class Weapon:
    def __init__ (self, weapon):
        self.name = weapon['name']
        self.exp = weapon['exp']
        self.level = weapon['level']
        self.minDmg = weapon['minDmg']
        self.maxDmg = weapon['maxDmg']
        self.accuracy = weapon['accuracy']
        self.avoid = weapon['avoid']
        self.parry = weapon['parry']
        self.minAbs = weapon['minAbs']
        self.maxAbs = weapon['maxAbs']
        self.endurance = weapon['endurance']
        self.createdAs = weapon
    def __repr__():
    	return "[" + str(self.level) + "]" + self.name