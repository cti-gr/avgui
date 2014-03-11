import sys, hashlib, os, requests
from configparser import SafeConfigParser
from uuid import getnode

def register():
	for argument in sys.argv:
		print("Argument: " + str(argument))
	# get mac address
	mac_address = getnode()
	
	# get uuid created upon installation
	confileName = os.getcwd() + "/conf/config.ini"
	conf = SafeConfigParser()
	conf.read(confileName)
	avguuid = conf.get('uuid', 'avguuid')
	
	# input avguuid and mac_address to sha512 --> globalUUID
	global_uuid = hashlib.sha512()
	global_uuid.update(str(mac_address).encode("utf"))
	global_uuid.update(str(avguuid).encode("utf"))
	globalUUID = global_uuid.hexdigest()
	print("Will now post: a) the email addresss: " + sys.argv[1] + "the sha512 hash of the password: " + str(sys.argv[2]) + "... and the global uuid: " + str(globalUUID))
	
	# send:
	# a) user email
	# b) user password
	# c) globalUUID

register()
