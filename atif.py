
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
linker.parse()
linker.filter()
linker.toCSV("./data/all_options_atif.csv")

filtered	= linker.filterOr([["A", "Natural light in the stair well"]])

##
# Print stuff
##
print(len(linker.chains))
print(len(filtered.chains))

