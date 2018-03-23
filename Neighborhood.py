from House import House
from Observer import Observer

###########################################
# Creates the neighborhood
#
# @param Observer
###########################################
class Neighborhood(Observer):
	neighborhood = [[0 for y in range(14)] for x in range(10)]


	def __init__(self):
		self.monster_count = 0
		self.neighborhood = [[0 for y in range(15)] for x in range(10)]
		for a in range(0, 10):
			
			for b in range(0,15):
				
				if a == 3 or a == 6:
					if b == 11 or b == 12 or b == 13:
						self.neighborhood[a][b] = "street"
						continue
						
					if b % 2 == 1:
						self.neighborhood[a][b] = "yard"
						continue
					else:
						self.neighborhood[a][b] = House()
					self.neighborhood[3][14] = "yard"
				elif a == 0 or a == 9:
					if b % 2 == 1:
						self.neighborhood[a][b] = "yard"
					else:
						self.neighborhood[a][b] = House()
				elif a== 1 or a == 2 or a == 7 or a == 8:
					self.neighborhood[a][b] = "street"
					if b == 14 and (a == 1 or a == 8):
						self.neighborhood[a][b] = "yard"
					elif (a == 2 or a == 7) and b == 14:
				
						self.neighborhood[a][b] = House()
				else:
				
					self.neighborhood[a][b] = "yard"
					self.neighborhood[a][11] = "street" 
					self.neighborhood[a][12] = "street" 
					self.neighborhood[a][13] = "street"
					self.neighborhood[4][14] = House()
				if isinstance(self.neighborhood[a][b], House):
					self.neighborhood[a][b].setObservers() 
		 			self.monster_count = self.monster_count + self.neighborhood[a][b].getNumMonsters()
					self.neighborhood[a][b].add_observer(self)
	

	def getPos(self, x, y):
		if self.neighborhood[x][y] == "street":
			print("You are in the street\n")
			return "street"
		elif self.neighborhood[x][y] == "yard":
			print("You are in someone's yard!\n")
			return "yard"
		elif self.neighborhood[x][y] == "House":
			print("You have cleared this house already!\n")
			return "House"
		else:
			print("You're at a house.\n")
		
	def setLocation(self, xPos, yPos):
		self.neighborhood[xPos][yPos] = "House"

	def getMonsterNumber(self):
		
		return self.monster_count
		
	def getHouse(self, xPos, yPos):
		return self.neighborhood[xPos][yPos]

	def update(self, house):
		self.monster_count = self.monster_count - 1
		if (self.monster_count == 0):
			pass

