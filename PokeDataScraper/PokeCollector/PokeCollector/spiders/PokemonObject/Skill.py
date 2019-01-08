
from enum import Enum
from CommonInterface import BaseType


# skill type
# There  are more subtype, such as powder, weather change, not take into consideration so far
class MoveCategory(Enum):
	UNDEFINED = 0
	SPECIAL = 1
	PYHSICAL = 2
	STATUSMOVE = 3

# status change
class Status(Enum):
	NORMAL = 0
	BURN = 1
	POSION = 2
	CONFUSE = 3
	PARALYZE = 4
	SLEEP = 5
	FREEZE = 6
	SCARED = 7

# initiate level
class MoveSequence(Enum):
	THREE_SLOW = 0
	TWO_SLOW = 1
	ONE_SLOW = 2 
	NORMAL = 3
	ONE_FAST = 4
	TWO_FAST = 5
	THREE_FAST = 6

# Affect attribute
class MoveBase():
	def __init__(self):
		self.MoveName = ""
		self.MoveCategory = MoveCategory.UNDEFINED
		self.hitRate = 1 # 0-100%
		self.sequence = MoveSequence.NORMAL

	def __init__(self, name, cate = MoveCategory.UNDEFINED, hitRate = 1, seq=MoveSequence.NORMAL):
		self.MoveName = name
		self.hitRate = hitRate
		self.sequence = seq


#inheretence skill base type for 3 kind of skill type, it may have special effect as well
class PhysicalMove(MoveBase):
	def __init__(self, name, hitRate, seq, power, cate=MoveCategory.PYHSICAL):
		MoveBase.__init__(self, cate, hitRate, seq)
		self.power = power


# special type, it may need status change as well
class SpecialMove(MoveBase):
	def __init__(self, name, hitRate, seq, power, cate=MoveCategory.SPECIAL):
		MoveBase.__init__(self, name, cate, hitRate, seq)
		self.power = power

# temp solution is using a string to describe the affect
class StatusMove(MoveBase):
	def __init__(self, name, hitRate, seq, cate=MoveCategory.STATUSMOVE, affect=""):
		MoveBase.__init__(self, name, cate, hitRate, seq)
		self.affect = affect
