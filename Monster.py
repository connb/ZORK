from Observable import Observable

###########################################
# Provides stats for Monsters and persons
# 
# @param Observable
###########################################
class Monster(Observable):

	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.atk

	def getName(self):
		return self.name

	def getDead(self):
		return self.dead

	def die(self):
		self.update_observers(self)
