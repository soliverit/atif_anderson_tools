import csv
from .linker_chain	import LinkerChain
class AtifLinker():
	def __init__(self, labels):
		self.labels	= labels.copy()
		self.chains	= []
	def parse(self):
		links1		= []
		links2		= []
		with open("./data/atif_all.csv") as file:
			csvFile	= csv.reader(file)
			for row in csvFile:
				links1.append(row)
		with open("./data/atif_all_2.csv") as file:
			csvFile	= csv.reader(file)
			for row in csvFile:
				links2.append(row)
		for link1 in links1:
			linkCount	= 0
			for link2 in links2:
				if link1[1] == link2[0]:
					self.append(LinkerChain([link1[0], link1[1], link2[1]]))
					linkCount += 1
			if linkCount == 0:
				self.append(LinkerChain([link1[0], link1[1]]))
		self.stripValues()
	def stripValues(self):
		for chain in self.chains:
			for id in range(len(chain.values)):
				chain.values[id] = chain.values[id].replace("\n","").replace("\r", "")
	def toCSV(self, path):
		with open(path, "w", newline='') as file:
			csvFile	= csv.writer(file)
			for chain in self.chains:
				csvFile.writerow(chain.values)
	def filter(self):
		newChainList	= []
		for chain in self.chains:
			duplicate = False
			for otherChain in newChainList:
				if chain == otherChain:
					duplicate = True
					break
			if not duplicate:
				newChainList.append(chain)
		self.chains	= newChainList
	def append(self, chain):
		self.chains.append(chain)
	def filterOr(self, filters):
		newLinker	= self.__class__(self.labels)
		for filter in filters:
			labelID	= self.labels.index(filter[0])
			for chain in self.chains:
				if labelID < len(chain.values):
					if chain.values[labelID] == filter[1]:
						newLinker.append(chain)
		return newLinker