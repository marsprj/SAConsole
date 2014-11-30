#coding=utf-8

import wx
import logging
import tarfile
import threading

class UntarThread(threading.Thread):

	def __init__(self, tar_path, untar_dir, logPanel):
		threading.Thread.__init__(self)
		self.tar_path = tar_path
		self.untar_dir = untar_dir

		self.logPanel = logPanel
		self.timeToQuit = threading.Event()
		self.timeToQuit.clear()


	def stop(self):
		self.timeToQuit.set()

	def run(self):
		#tar_path = "/home/renyc/download/postgis-1.5.8.tar.gz"
		#sa_home = "/home/renyc/code/python/untar"

		try:
			tar = tarfile.open(self.tar_path)
			names = tar.getnames()
			for name in names:
				tar.extract(name, self.untar_dir)
				wx.CallAfter(self.logPanel.Append,name)
				#self.logPanel.txtTar.AppendText('----------------------\n')
				#self.logPanel.txtTar.AppendText(name)
				#logPanel.txtTar.AppendText('\n')

			tar.close()

		except ExtractError, e:
			print "ExtractError e"
			#self.showMessageBox(u'tar包解压失败', u'错误')

		print '安装完成.................'
