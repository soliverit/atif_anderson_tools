##
# Includes
##
## Project
from lib.requester 		import Requester
##
# Create a request and start EC3 session
##
requester 	= Requester()
requester.login("soliver.i.t@gmail.com", "SpaceballsThePassword")
##
# Get the first 100 (EC3 limit) matching materials then select the first
##
js		= requester.materials({"plant_or_group__name__like": "r`edwood"}).json()
record	= js[0]
##
# Print formatted key value pairs. Just a clean way to review
# the record values. 
#
# E.g
#	name:	concrete
#	gwp:	100
##
for key in list(record):
	##
	# This is purely personal preference. If the key length
	# isn't based on the max, the table's messy. 
	#
	# Note: I figure 25 is good enough for most but max([len(key) for key in list(record)]) would
	#		find the right lenght.
	##
	value	= str(record[key])
	while len(key) < 30:
		key += " "
	print(key + ": " + value)


requester.logout()