from Ghoul import Ghoul
from Vampire import Vampire
from Werewolf import Werewolf
from Zombie import Zombie
from Monster import Monster
from Person import Person
from Observer import Observer
from Observable import Observable
import random

###########################################
# 
#
# @param Observer, Observable
###########################################
class House(Observer, Observable):
	def __init__(self):
		#List of monsters in the house
		self.monster = [] 
		self.p = Person()
		#random number of monsters in house
		self.ran = random.randint(1,10)
		self.observers = []
		#instantiates monster list
		for x in range (0,self.ran):
			self.monster = self.monster + random.sample([Ghoul(), Vampire(), Werewolf(), Zombie(), self.p], 1)
			
	
	def getNumMonsters(self):
		return self.ran
	
	def getMonsters(self):
		names = ""
		for x in range (0,self.ran):
			
			names = names + " " + self.monster[x].getName()
		print("\nThese are the Monsters left in the room:")
		print(names + "\n")

	def attacked(self, hit, item):
		for x in range (0 , self.ran):
			if self.monster[x] == self.p:
				pass
			else:
				self.monster[x].attacked(hit, item)
				if self.monster[x].getDead():
					self.monster[x] = Person()

	def attack(self):
		self.total = 0
		for x in range (0 , self.ran):
			if self.monster[x] == 0:
				pass
			else:
				self.total = self.total + self.monster[x].getAttack()
		return self.total

	def clear(self):
		for x in range(0,self.ran):
			if not isinstance(self.monster[x], Person):
				return False
		return True

	def setObservers(self):
		for x in range (0,self.ran):
			self.monster[x].add_observer(self)
	
	def update(self, monster):
		if isinstance(monster, Monster):
			self.monster.remove(monster)
			self.monster.append(Person())
		self.update_observer(self)
