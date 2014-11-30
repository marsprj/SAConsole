#coding=utf-8

import wx
import logging
import tarfile
import threading

class UntarThread(threading.Thread):

	def __init__(self, tar_path, untar_dir, window, logPanel):
		threading.Thread.__init__(self)
		self.tar_path = tar_path
		self.untar_dir = untar_dir
		self.window = window
		self.logPanel = logPanel

		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()


	def stop(self):
		self.timeToQuit.set()

	def run(self):
		try:
			tar = tarfile.open(self.tar_path)
			names = tar.getnames()
			for name in names:
				tar.extract(name, self.untar_dir)
				wx.CallAfter(self.logPanel.Append,name)

			tar.close()

		except ExtractError, e:
			print "ExtractError e"
			#self.showMessageBox(u'tar包解压失败', u'错误')

		wx.CallAfter(self.window.ShowFinishBox,'')
