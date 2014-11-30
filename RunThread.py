#coding=utf-8

import wx
import logging
import tarfile
import threading

class RunThread(threading.Thread):

	def __init__(self, cmd):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()


	def stop(self):
		self.timeToQuit.set()

	def run(self):
		print self.cmd
		os.popen(self.cmd)