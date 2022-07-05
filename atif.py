import csv
from lib.atif_linker import AtifLinker
import os
os.chdir("C:\\repos\\anderson_atif_projects")
linker = AtifLinker()
linker.parse()
print(len(linker.chains))
linker.filter()
print(len(linker.chains))
linker.toCSV("./data/all_options_atif.csv")
exit()
#######################################

##
# Includes
##
## Project
from lib.comfort_parser import ComfortParser
##
# Parse the lists
##
import os
##
# Parse the input data
##
parser	= ComfortParser("c:/repos/anderson_atif_projects/data/atif.csv")
##
# Some test stuff
##
12