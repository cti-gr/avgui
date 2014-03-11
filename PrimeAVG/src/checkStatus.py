#!/usr/bin/python3

from configparser import SafeConfigParser
import os

def checkStatus():
	
	print("checking status with uid: " + str(os.getuid()))

	confileName = os.getcwd() + "/conf/config.ini"
	conf = SafeConfigParser()
	conf.read(confileName)
	if conf.get('Registered', 'isRegistered') == "False":
		print("Not Registered, will now register.")
		exit(14)
	else:
		print("The user is registered, will try to submit issue.")
		exit(13)


checkStatus()

