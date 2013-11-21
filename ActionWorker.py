# -*- coding: utf-8 -*-

"""
Worker for start scripts
"""

import Worker
import subprocess

class ActionWorker(Worker.Worker):
	def __init__(self, action_queue, action_command):
		Worker.Worker.__init__(self, action_queue)
		self._command_template = action_command

	# Function for call external system programms
	def _action(self, data):
		shell_command = self._command_template.replace("<IP>", data)
		try:
			system_pipe = subprocess.Popen(shell_command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = None)
			system_pipe.poll()
		except:
			# May be some log here 
			pass
		
