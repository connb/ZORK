from Bar import Bar
from Straw import Straw
from Bomb import Bomb
from Kiss import Kiss
from collections import Counter
import random

###########################################
# Keeps track of the Player's Stats
#
###########################################
class Player:
	
	def __init__(self):
		self.health = random.randint(200, 300)
		self.attack = random.randint(10,20)
		self.inventory = []
		for x in range(0,10):
			self.bar = Bar()
			self.straw = Straw()
			self.bomb = Bomb()
			self.kiss = Kiss()
			self.inventory = self.inventory + random.sample([self.bomb, self.kiss, self.straw, self.bar], 1)
		
	def status(self):
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("\n***** Player Stats *****")
		print("Health:{} Attack:{}\n".format(self.health, self.attack))

	def Inventory(self):
		self.sInventory = []
		for x in range(0,10):
			self.sInventory.append(self.inventory[x].getString())
		print("\n***** Weapon Inventory *****")
		print(sorted(self.sInventory))
		print(" \n")

	def checkInventory(self, item):
		for x in range(0,10):
			if item == self.inventory[x].getString():
				return True
		return False

	def getMult(self, item):
		for x in range(0,10):
			if item == self.inventory[x].getString():
				self.inventory[x].used()
				y = self.inventory[x].getMult()
				if self.inventory[x].getUse() <= 0:
					self.inventory[x] = self.kiss
				return y

	def getAttack(self):
		return self.attack

	def getHealth(self):
		return self.health
			
	def atkBomb(self):
		return self.attack * self.getMult("Nerd Bomb")
	
	def atkBar(self):
		return self.attack * self.getMult("Chocolate Bar")
	 
	def atkStraw(self):
		return self.attack * self.getMult("Sour Straw")
	
	def atkKiss(self):
		return self.attack 

	def attacked(self, hit):
		self.health -= hit
	
	def generateItems(self, num):
		for x in range (0, 10):
			if self.inventory[x] == self.kiss:
				self.inventory.remove(self.kiss)
				self.inventory = self.inventory + random.sample([self.bomb,self.kiss, self.straw], 1)
