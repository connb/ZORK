#!/usr/bin/env python

from Neighborhood import Neighborhood
from Player import Player

###########################################
# Controls the major functionality of
# the game such as movement, attack, win/loss
#
###########################################
class Game():

	player = Player()
	Neighborhood = Neighborhood()
	def __init__(self):
		first = 1
		self.player = Player()
		self.xPos = 1
		self.yPos = 0
		self.Neighborhood = Neighborhood()
		self.won = False
		
	#Method that controls all movement as well as miscellaneous commands while in the neighborhood
	def move(self):
		loop = 4
		while loop == 4:
			first = raw_input("\nWhich direction would you like to go?\n")
	
			if first == "north" or first == "North":
				if self.yPos == 14:
					print("You can't go any further North!")
				else:
					self.yPos +=1
			elif first == "east" or first == "East":
				if self.xPos == 9:
					print("You can't go any further East!")
				else:
					self.xPos +=1
			elif first == "south" or first == "South":
				if self.yPos == 0:
					print("You can't go any further South!")
				else:
					self.yPos -=1
			elif first == "west" or first == "West":
				if self.xPos == 0:
					print("You can't go any further West!")
				else:
					self.xPos -=1

			elif first == "help":
				print("1. Type 'north', 'south', 'east' or 'west' to move and the game will tell you if you're at a house, in a yard, or on the street)")
				print("2. If you decide you would like to start a new game then type 'quit' to exit the current game")
				print("3. Type 'info' if you want to know your current health/attack, inventory, and number of monsters left")

			elif first == "quit" or first == "Quit":
				self.end()

			elif first == "info" or first == "Info":
				self.player.status()
				self.player.Inventory()
				print("Total number of Monsters remaining in the Neighborhood: " + str(self.Neighborhood.getMonsterNumber()) + "\n")
			
			else:
				print("Please enter a valid direction")
			pos = self.Neighborhood.getPos(self.xPos, self.yPos)

			if pos == "street" or pos == "yard" or pos == "House":
				pass

			else: 
				second = raw_input("Would you like to enter this house?\n")
				if second == "yes" or second == "Yes":
					self.attackPhase(self.xPos, self.yPos)
				else:
					print("\n")
				
	#The game has ended and the winning or losing message is displayed
	def end(self):
		if self.won == True:
			print("Congratulations! You won the game!")
		else:
			print("Sorry, you lost the game. Come back and try again!")
		import os
		quit(1)

	#Provides the attack functionality for the user's input
	def attackPhase(self, xPos, yPos):
		print("You've entered the house! Your current stats are:")
		self.loop = 5

		while self.loop == 5:
			self.player.status()
			self.player.Inventory()
			self.loop = 5
			self.Neighborhood.getHouse(xPos,yPos).getMonsters()	
			 
			atk = 1
			self.item = raw_input("What type of candy do you want to use to attack?\n")

			if self.item == "Hershey Kiss" or self.item == "hershey kiss":
				if self.player.checkInventory("Hershey Kiss"):
					atk = self.player.atkKiss()
					self.loop = 6
				else:
					print("You don't have any more of this item!")

			elif self.item == "Chocolate Bar" or self.item == "chocolate bar":
				if self.player.checkInventory("Chocolate Bar"):
					atk = self.player.atkBar()
					self.loop = 6
				else:
					print("You don't have any more of this item!")

			elif self.item == "sour straw" or self.item == "Sour Straw":
				if self.player.checkInventory("Sour Straw"):
					atk = self.player.atkStraw()
					self.loop = 6
				else:
					print("You don't have any more of this item!")

			elif self.item == "Nerd Bomb" or self.item == "nerd bomb":
				if self.player.checkInventory("Nerd Bomb"):	
					atk = self.player.atkBomb()
					self.loop = 6
				else:
					print("You don't have any more of this item!")

			elif self.item == "info":
				print("\n")
				self.Neighborhood.getHouse(xPos,yPos).getMonsters()
				self.player.status()
				self.player.Inventory()

			elif self.item == "run":
				print("You ran out of the house!")
				self.loop = 4

			elif self.item == "help":
				print("1. Type 'Chocolate Bar', 'Hershey Kiss', 'Sour Straw', or 'Nerd Bomb' to attack")
				print("2. If you feel you can't take on this house currently, type 'run' and you will be able to escape back into the neighborhood")
				print("3. Type 'info' to display your current health/attack, inventory, and types of monsters left in the current house")
			else:
				print("please input a valid item\n")
			while self.loop == 6:
				
				self.Neighborhood.getHouse(xPos,yPos).attacked(atk, self.item)
				self.mAtk = self.Neighborhood.getHouse(xPos,yPos).attack()	
				
				self.player.attacked(self.mAtk)
				self.loop = 5
				if self.player.getHealth() <= 0:
					self.won = False
					self.end()
				if self.Neighborhood.getHouse(xPos,yPos).clear():
					print("All the monsters in this house are people again! Your reward is extra weapons")
					i = self.Neighborhood.getHouse(xPos,yPos).getNumMonsters()
					if(self.Neighborhood.getMonsterNumber() <= 0):
						self.won = True
						self.end()
					self.player.generateItems(i)
					self.Neighborhood.setLocation(xPos, yPos)
					self.loop = 7

#The beginning invocation and description of the program
print("********************************************************************************************")
print("\nIt seemed like a normal Halloween Eve. You bought a lot of candy,\nate a lot of candy, and went to bed early. You had a lot trick-or-treating\nto do the next day.\n\nUnfortunately, when you woke up you discovered\nthat the world was not how you left it. Batches of bad candy had transformed\nyour friends and neighbors into all sorts of crazy monsters.\nSomehow you missed the tainted candy; it is therefore up to you to\nsave your neighborhood and turn everyone back to normal.\n\nType a direction ('north', 'south', 'east', 'west') to begin.\nOnce you've found a house, you have the option to enter and face the monsters inside,\nor you may continue to another location. If at any time you need help, simply type 'help'.\n")				
print("********************************************************************************************\n")

g = Game()
g.move()
