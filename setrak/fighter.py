import random

class Fighter:
    def __init__ (self, char):
        try:
            self.name = char['name']
            self.exp = char['exp']
            self.level = char['level']
            self.hp = char['hp']
            self.minDmg = char['minDmg']
            self.maxDmg = char['maxDmg']
            self.minWeapon = char['minWeapon']
            self.maxWeapon = char['maxWeapon']
            self.accuracy = char['accuracy']
            self.avoid = char['avoid']
            self.parry = char['parry']
            self.minAbs = char['minAbs']
            self.maxAbs = char['maxAbs']
            self.endurance = char['endurance']
            self.createdAs = char
        except:
            self.name, self.exp, self.level, self.hp, self.minDmg, self.maxDmg = 'Vatte', 0, 1, 20, 5, 5
            self.minWeapon, self.maxWeapon, self.accuracy, self.avoid,self.parry = 0, 0, 20, 10, 10
            self.minAbs, self.maxAbs, self.endurance = 0, 0, 5

    def gainExp(self, exp):
        self.exp += exp

    def attack(self):
        return random.randint(self.minDmg + self.minWeapon, self.maxDmg + self.maxWeapon)

    def getAccuracy(self):
        return self.accuracy
    def getAvoid(self):
        return self.avoid
    def getParry(self):
        return self.parry

    def bleed(self, amount):
        amount = amount - random.randint(self.minAbs, self.maxAbs)
        amount = amount if amount > 0 else 1
        self.hp -= amount
        return amount

    def health(self):
        return self.hp

    def heal(self, amount):
        self.hp += amount

    def printHealth(self):
        print(self.name + " health: " + str(self.hp))

    def getTired(self, current_round):
        if self.isTired(current_round):
            self.parry = int(self.parry * 0.8)
            self.avoid = int(self.avoid * 0.8)
        return current_round > self.endurance

    def isTired(self, current_round):
        return current_round > self.endurance

    def printStats(self):
        print("Name", self)
        print("level:",  self.level, "(" + str(self.exp) + ")")
        print("hp:", self.hp)
        print("Damage:", self.minWeapon, '-', self.maxWeapon, '->', self.minDmg + self.minWeapon, '-', self.maxDmg + self.maxWeapon)
        print("accuracy:",   self.accuracy)
        print("avoid:",  self.avoid)
        print("parry:",  self.parry)
        print("Absorb:", self.minAbs, '-', self.maxAbs)
        print("endurance:",  self.endurance)

    # Later, a JSON object 
    def equip(self, dmg):
        self.weapondamage = dmg
    def __repr__(self):
        return ("[%s]%s" % (str(self.level), self.name))