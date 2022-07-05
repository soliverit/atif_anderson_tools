
##
# Includes
##
## Native
import csv
import os
## Project
from lib.atif_linker 	import AtifLinker
from lib.linker_chain	import LinkerChain
## Do stuff in the project working directory
os.chdir("C:\\repos\\anderson_atif_projects")
##
# Do stuff
##
linker = AtifLinker(["A", "B", "C"])
length	= len(linker.chains)
linker.parse()
linker.filterUnique()
linker.toCSV("./data/all_options_atif.csv")

orFiltered	= linker.filterOr(
	[
		["A", "Wardrobe space"],
		["B", "Sufficient storage"]
	]
)
andFiltered	= linker.filterAnd(
	[
		["A", "Wardrobe space"],
		["B", "Sufficient storage"]
	]
)
##
# Print stuff
##
print(len(length))				# All options
print(len(linker.chains))		# Unique
print(len(orFiltered.chains))	# OR filtered
print(len(andFiltered.chains))	# AND filtered

