
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
linker = AtifLinker()
linker.parse()
print(len(linker.chains))
linker.filter()
print(len(linker.chains))
linker.toCSV("./data/all_options_atif.csv")
