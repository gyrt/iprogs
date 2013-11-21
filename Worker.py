# -*- coding: utf-8 -*-

"""
Basic worker class for python threads that will count packets and start scripts
"""

import threading, os

class Worker(threading.Thread):
	def __init__(self, work_queue):
		threading.Thread.__init__(self)
		self._work_queue = work_queue
		self.daemon = True
		self._start_bit = True

	def run(self):
		while self.is_started():
			data = self._work_queue.get(True)
			self._action(data)
		os.exit(0)	

	# Function for some actions. Will be redefined in other classes
	def _action(self, data):
		pass

	# Functions for thread 
	def is_started(self):
		return self._start_bit

	def set_stopped(self):
		self._start_bit = False
