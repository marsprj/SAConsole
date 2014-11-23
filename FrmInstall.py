#coding=utf-8

import wx
import os
import shutil
import tarfile
import SAConfig

class FrmInstall(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title=u'拷贝数据',size=(500,170),style=(wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR)^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))

		panel = wx.Panel(self)

		self.tar_path = ''
		self.sa_home = SAConfig.GetValue('sa_home')

		wx.StaticText(panel,label=u'安 装 包:', pos=(20,20))
		self.txtTar = wx.TextCtrl(panel, pos=(90,18), size=(300,25), style=wx.TE_READONLY)
		self.txtTar.SetBackgroundColour('#FFFFFF')
		btnTar = wx.Button(panel, label=u'选择文件', pos=(400,15), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onSelectTar, btnTar)

		wx.StaticText(panel,label=u'安装路径:', pos=(20,58))
		self.txtFolder = wx.TextCtrl(panel, pos=(90,60), size=(300,25), style=wx.TE_READONLY)
		self.txtFolder.SetBackgroundColour('#FFFFFF')
		btnFolder = wx.Button(panel,label=u'选择路径', pos=(400,55), size=(80,30))		
		self.Bind(wx.EVT_BUTTON, self.onSelectFolder, btnFolder)
		self.txtFolder.SetValue(self.sa_home)

		btnInstall = wx.Button(panel, label=u'安装程序', pos=(180,100), size=(120,30))
		self.Bind(wx.EVT_BUTTON, self.onInstall, btnInstall)

	def onSelectTar(self, event):
		dlg = wx.FileDialog(self, u'选择安装包', self.tar_path, '', '*.tar.gz', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.tar_path = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtTar.SetValue(self.tar_path)
		dlg.Destroy()

	def onSelectFolder(self, event):
		dlg = wx.DirDialog(self, u'选择安装路径',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			self.sa_home = dlg.GetPath()
			self.txtFolder.SetValue(self.sa_home)
		dlg.Destroy()

	def onInstall(self, event):
		# check whether tar file exists
		if(os.path.isfile(self.tar_path)==False):
			self.showMessageBox(u'安装文件 ['+self.tar_path+u'] 不存在', u'警告')
			return;

		if(os.path.isdir(self.sa_home)==False):
			self.showMessageBox(u'目录 ['+self.sa_home+u'] 不存在', u'警告')
			return;

		try:
			tar = tarfile.open(self.tar_path)
			names = tar.getnames()
			for name in names:
				tar.extract(name, self.sa_home)
			
			tar.close()

			self.setSaHomeEnv(self.sa_home)

			self.showMessageBox(u'安装完成', u'提示')
		except ExtractError, e:
			print "ExtractError e"
			self.showMessageBox(u'tar包解压失败', u'错误')
		

	def showMessageBox(self, message, title):
		dlg = wx.MessageDialog(self, message, title, wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def setSaHomeEnv(self, sa_home):
		pass