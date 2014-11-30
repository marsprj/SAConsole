#coding=utf-8

import os
import wx
import threading

class RunThread(threading.Thread):

	def __init__(self, cmd, window):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.window = window
		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()


	def stop(self):
		self.timeToQuit.set()

	def run(self):
		print self.cmd
		os.popen(self.cmd)
		
		wx.CallAfter(self.window.OnRunFinish,'')
