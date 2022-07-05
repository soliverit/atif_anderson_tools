import csv
class Linker():
	def __init__(self):
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
			self.chains.append(LinkerChain([link1[0], link1[1]]))
			for link2 in links2:
				if link1[1] == link2[0]:
					self.chains.append(LinkerChain([link1[0], link1[1], link2[1]]))
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
				
class LinkerChain():
	def __init__(self, values):
		self.values	= [value for value in values]