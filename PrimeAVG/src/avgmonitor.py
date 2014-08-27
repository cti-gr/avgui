#!/usr/bin/python3

import simpledaemon
import logging
import time
import subprocess
import sys
import os
import signal
import config


class AVGMonitor(simpledaemon.Daemon):
	
	if "/usr/share" in os.getcwd():
		default_conf = os.path.expanduser("~") + '/.avgui/log/hellodaemon.conf'
	else:
		default_conf = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/log/hellodaemon.conf'
	
	section = 'hello'

	print(default_conf)	


	def run(self):
		print(sys.argv[1:])
		while True:
			out = subprocess.call(["ps", "-C", "avgd"])
			if out == 1:
				os.kill(int(sys.argv[2]), signal.SIGALRM)
				sys.exit(1)
			else:
				pass
			time.sleep(1)

if __name__ == '__main__':
	AVGMonitor().main()
