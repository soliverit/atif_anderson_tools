##
# Includes
##
## Native
import csv
##
# ComfortParser: Parse input lists to object
##
class ComfortParser():
	##
	# Constructor: 
	##
	def __init__(self, path):
		self.path			= path	# Path to input file
		self.features		= {}	# Dictioanry of input list values like {"name": ["Atif", "Anderson"],"age": [21, 21],..}
		self.headers		= []	# A explicitly ordered list of headers (CSV column names in order of appearance)
		self.listHeaders	= []	# An explicitly ordered list of headers that are list names, only. No "_link" columns
		self.parse()			# Read the input file
	##
	# Parse the ipnut file to the dictionary
	##
	def parse(self):
		##
		# Read the CSV file into an array of dictionaries
		##
		with open(self.path, newline='', encoding='utf-8-sig') as csvfile:
			reader 			= csv.DictReader(csvfile)
			##
			# Extract headers in hash/dictioanry keys for selecting related
			# values from the CSV rows.
			#
			# Changes the structure from an array of dicts [{"name": "Dave"}, {"age": 21},..]
			# to a dictionary of arrays {"name": ["Dave", "Tahir"], "age": [21, 21],..}
			#
			# Info: The list(reader.fieldnames) makes a safe copy of the
			#		field name array. Without a copy, changing one would
			#		change the other because headers and fieldnames would
			#		be pointing to the same array.
			##
			self.headers	= list(reader.fieldnames)
			for header in reader.fieldnames:
				self.features[header]	= []
			##
			# Populate the dictionary arrays and header arrays (all and list name only)
			##
			for row in reader:
				for header in reader.fieldnames:
					value	= row[header]	# Note: there's no need for this line but it's easier to read with it.
					if value or "_link" in header:
						self.features[header].append(value)
					if "_link" not in header:
						self.listAliases.append(header):
		##
		# Identify if a row record in a list is connected to the next list.
		#
		# Each list header is followed by a columne named after the list with "_link"
		# appended to the name. If the link cell has a value, it is considered to be
		# linked to the next list. 
		#
		# Returns:	Boolean, row in one list is attached to the other list.
		##
		def isConnectedToNextList(self, header, row):
			##
			# Some error handling
			#
			# Normally wouldn't add these but it's helpful for someone less familiar
			# with the class.
			##
			if header not in self.headers:
				raise "Header not found in input headers (" + ", ".join(self.headers) + ")"
			if header == self.headers[-2]:
				raise "Header is the last list, there is no following list to connect to"
			##
			# Get the result
			#
			# Note: The [row] length in lists are not identical so if 
			# list A has 4 entries and B 5, you can call with "B", 5 and
			# you'll get the result but, if you tried "A", 5, an index
			# out of bounds error will occur.
			##
			return self.features[header + "_link"][row]  != ""
		##
		# Create a list of every possible chain list
		##
		def buildChain(self):
			chains	= []
			for header in self.list:
				chain	= ComfortChain(header)
				if "_link" not in header:
					for row in self.features[header]:
				
##
# A linked list type structure that binds list entries to entries
# in the other lists
##
class ComfortChain():
	def __init__(self, alias):
		self.alias		= alias
		self.chained	= []
				

		