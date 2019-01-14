from enum import Enum

# BaseType Class define the type for skills and pokemons
class BaseType(Enum):
	UNDEFINED = 0
	FIRE = 1
	WATER = 2
	GRASS = 3
	ELECTRIC = 4
	NORMAL = 5
	ICE = 6
	POSION = 7
	FIGHTING = 8
	FLYTING = 9
	GROUND = 10
	PSYCHIC = 11
	ROCK = 12
	BUG = 13
	DROGAN = 14
	GHOST = 15
	DARK = 16
	STEEL = 17
	FAIRY = 18

# this is for skill object, e.g. attack decrease by 1 level
class IndividualValue(Enum):
	ATTACK = 0
	DEFENSE = 1
	SPECIAL_ATTACK = 2
	SPECIAL_DEFENSE = 3
	SPEED = 4
	HEALTH = 5

# this is for pokemon object
class IndividualValues():
	def __init__(self, phyAtt=0, speAtt=0, phyDef=0, speDef=0, spd=0, hp=0):
		self.physicalAttack = phyAtt
		self.physicalDefense = phyDef
		self.specialAttack = speAtt
		self.specialDefense = speDef
		self.healthPoint = hp
		self.speed = spd