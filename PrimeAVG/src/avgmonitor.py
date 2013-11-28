#!/usr/bin/python3

import simpledaemon
import logging
import time
import subprocess
import sys
import os
import signal

class AVGMonitor(simpledaemon.Daemon):
	default_conf = '../log/hellodaemon.conf'
	section = 'hello'

	def run(self):
		print(sys.argv[1:])
		while True:
			#for i in range(len(sys.argv)):
			#	logging.info("argv[" + str(i) + "]" + " " + str(sys.argv[i]))
			#logging.info(str(sys.argv[1]))
			#logging.info(str(len(sys.argv)))
			out = subprocess.call(["ps", "-C", "avgd"])
			if out == 1:
				os.kill(int(sys.argv[2]), signal.SIGALRM)
				sys.exit(1)
			else:
				pass
			time.sleep(1)

if __name__ == '__main__':
	AVGMonitor().main()
