class LinkerChain():
	def __init__(self, values):
		self.values	= [value for value in values]
	def __eq__(self, otherChain):
		if len(self.values) != len(otherChain.values):
			return False
		for id in range(len(self.values)):
			if self.values[id] != otherChain.values[id]:
				return False
		return True