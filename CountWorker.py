# -*- coding: utf-8 -*-

"""
Worker for packet couters
"""

import Worker
import dbm

class CountWorker(Worker.Worker):
	def __init__(self, packets_queue, action_queue, limit):
		Worker.Worker.__init__(self, packets_queue)
		self._action_queue = action_queue
		self._limit = limit
		self._database = dbm.open("/tmp/packets.dbm", "c")

	# Function for count packets
	def _action(self, data):
		ip_addr = data[0]
		packets = data[1]
		if self._database.has_key(ip_addr):
			self._database[ip_addr] = str(packets + int(self._database[ip_addr]))
		else:
			self._database[ip_addr] = str(packets)

		if self._database[ip_addr] >= self._limit:
			self._action_queue.put_nowait(ip_addr)
			self._database[ip_addr] = str(0)
