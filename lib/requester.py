##
# Includes
##
## Native
from requests	import get, post
##
# Requester: An OpenAPI interface (for EC3)
#
# Send requests and receive data from the EC3 database (or any DB if you change the BASE_URL).
##
class Requester():
	## API URL: It's for EC3 here but could be any data set
	BASE_URL 	= "https://etl-api.cqd.io/api/"
	## Default request headers. The API document adds these in the example https://etl-api.cqd.io/#/materials/get_materials
	HEADERS		=  {'content-type': 'application/json', 'accept': 'application/json'}
	##
	# Instantiate (the constructor method)
	##
	def __init__(self):
		# Dictionaries/hashes are more or less passed by reference. If
		# you set headers = self.__class__.HEADERS then change a value
		# in headers, self.__class__.HEADERS will be update. To prevent
		# that, the hash/dictionaries structure is cloned.
		self.headers	= self.__class__.HEADERS.copy()
	##
	# Login: Get an authorisation token and add it to the headers.
	##
	def login(self, username, password):
		request							= self.post("rest-auth/login", {"username": username, "password": password})
		self.headers["Authorization"] 	= "Bearer " + request.json()["key"]
		return request
	##
	# Logout: Tell EC3 to invalidate the authorisation key.
	##
	def logout(self):
		return self.post("rest-auth/logout", {})
	##
	# Materials: Get a list of materials using a filter.
	#
	# The method returns a list of up to 100 (EC3 limit, I think) based
	# on the filter criteria. The filter is applied to the parameter names
	# expected to be in the query response. 
	#
	# The API gives the following examples:
	# Find all mixes (by name): {base_path}/materials?name__like=mix
	# Find materials with 'PERFORMIX' in description: {base_path}/materials?description__like=PERFORMIX
	# Find all materials that Redwood plant makes: {base_path}/materials?plant_or_group__name__like=redwood
	# Find all materials that CalPortland makes: {base_path}/materials?plant_or_group__owned_by__name__like=CalPortland
	# Find all materials that Dupont plant makes: {base_path}/materials?plant_or_group__name__like=dupont&plant_or_group__owned_by__name__like=CalPortland
	# Sort all materials by manufacturer in ascending order: {base_path}/materials?sort_by=+plant_or_group__owned_by__name	
	#
	# Function reference: https://etl-api.cqd.io/#/materials/
	#
	# Inputs:
	#
	# filter:	A dictionary/hash of EC3 parameter names and values. {"name_like": "concrete"}, for example
	#
	##
	def materials(self, filter):
		return self.get("materials" + __class__.parametersToString(filter), {})
	##
	# Get requests: Requests that use the HTTP GET method.
	#
	# This request type is for retrieving things.
	#
	# Inputs:
	#
	# url:			The base URL. Note: filter strings are appended to this before
	#				calling get() or post(). See .materials() for an example.
	# parameters:	The hash/dictionary parameter set to be sent with the request
	#				like username and password in the .login() method
	##
	def get(self, url, parameters):
		return get(self.__class__.BASE_URL + url , json=parameters,  headers=self.headers)
	##
	# Post request: Requests that use the HTTP POST method.
	#
	# This request type creates things on the API server. The
	# login() method, for example, asks the server to create a 
	# new session for the user account 
	#
	# Inputs:
	#
	# url:			The base URL. Note: filter strings are appended to this before
	#				calling get() or post(). See .materials() for an example.
	# parameters:	The hash/dictionary parameter set to be sent with the request
	#				like username and password in the .login() method
	##
	def post(self, url, parameters):
		request	= post(self.__class__.BASE_URL + url, json=parameters, headers=self.headers)
		return request
	##
	# Hash/Dictionary to parameter string
	#
	# Warning: For some reason I couldn't get filter parameters to apply
	# when they were in the get()/post() parameters. Rather than waste 
	# more time, this method creates a URL parameter string that is
	# appended to request URLs. See materials() for example
	#
	#Inputs:
	#
	# parameters:	A hash/dictionary
	#
	# Outputs:
	#
	# string: A URL parameter string of the input has/dictionary (<base URL>?param_1=fire&param_2=water...)
	#
	##
	@staticmethod
	def parametersToString(parameters):
		parameterStrings	= []
		for key in list(parameters):
			parameterStrings.append(key + "=" + str(parameters[key]))
		return "?" + "&".join(parameterStrings)
		