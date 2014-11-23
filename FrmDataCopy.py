#coding=utf-8

import wx
import os
import shutil
import logging
import tarfile
import SAConfig
from PanelLog import LogPanel

class FrmDataCopy(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title=u'拷贝数据',size=(560,300),style=(wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR)^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))

		panel = wx.Panel(self)

		self.srcFile1 = '';
		self.srcFile2 = '';
		self.srcFile3 = '';
		self.srcFile4 = '';
		self.desFold = SAConfig.GetValue('sa_home')

		# Choose Source File
		wx.StaticText(panel, label=u'sa_03_2009_data:', pos=(20,20))
		self.txtData1 = wx.TextCtrl(panel, pos=(130,18), size=(320,25), style=wx.TE_READONLY)
		self.txtData1.SetBackgroundColour('#FFFFFF')
		btnSrc = wx.Button(panel, label=u'选择文件', pos=(460,15), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChoosFile1, btnSrc)
		#self.txtSrc.SetValue(self.srcFile);

		# Choose Source File
		wx.StaticText(panel, label=u'srgtools_data:', pos=(20,60))
		self.txtData2 = wx.TextCtrl(panel, pos=(130,58), size=(320,25), style=wx.TE_READONLY)
		self.txtData2.SetBackgroundColour('#FFFFFF')
		btnSrc = wx.Button(panel, label=u'选择文件', pos=(460,55), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChoosFile2, btnSrc)
		#self.txtSrc.SetValue(self.srcFile);

		# Choose Source File
		wx.StaticText(panel, label=u'nlcdmodis_data:', pos=(20,100))
		self.txtData3 = wx.TextCtrl(panel, pos=(130,98), size=(320,25), style=wx.TE_READONLY)
		self.txtData3.SetBackgroundColour('#FFFFFF')
		btnSrc = wx.Button(panel, label=u'选择文件', pos=(460,95), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChoosFile3, btnSrc)
		#self.txtSrc.SetValue(self.srcFile);

		# Choose Source File
		wx.StaticText(panel, label=u'beld3_data:', pos=(20,140))
		self.txtData4 = wx.TextCtrl(panel, pos=(130,138), size=(320,25), style=wx.TE_READONLY)
		self.txtData4.SetBackgroundColour('#FFFFFF')
		btnSrc = wx.Button(panel, label=u'选择文件', pos=(460,135), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChoosFile4, btnSrc)
		#self.txtSrc.SetValue(self.srcFile);


		# Choose Target Folder
		wx.StaticText(panel, label=u'目标路径:', pos=(20,190))
		self.txtDes = wx.TextCtrl(panel, pos=(130,188), size=(320,25), style=wx.TE_READONLY)
		self.txtDes.SetBackgroundColour('#FFFFFF')
		btnDes = wx.Button(panel, label=u'目标路径', pos=(460,185), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChooseDestination, btnDes)
		self.txtDes.SetValue(self.desFold);

		# Copy Button
		btnCopy = wx.Button(panel, label=u'拷贝数据', pos=(220,230), size=(120,30))
		self.Bind(wx.EVT_BUTTON, self.onCopy, btnCopy)


	def onChoosFile1(self, event):
		dlg = wx.FileDialog(self, u'选择数据文件', self.srcFile1, '', '*.tar.gz', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.srcFile1 = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtData1.SetValue(self.srcFile1)
		dlg.Destroy()

	def onChoosFile2(self, event):
		dlg = wx.FileDialog(self, u'选择数据文件', self.srcFile2, '', '*.tar.gz', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.srcFile2 = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtData2.SetValue(self.srcFile2)
		dlg.Destroy()

	def onChoosFile3(self, event):
		dlg = wx.FileDialog(self, u'选择数据文件', self.srcFile3, '', '*.tar.gz', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.srcFile3 = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtData3.SetValue(self.srcFile3)
		dlg.Destroy()

	def onChoosFile4(self, event):
		dlg = wx.FileDialog(self, u'选择数据文件', self.srcFile4, '', '*.tar.gz', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.srcFile4 = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtData4.SetValue(self.srcFile4)
		dlg.Destroy()

	def onChooseDestination(self, event):
		dlg = wx.DirDialog(self, u'选择复制路径',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			self.desFold = dlg.GetPath()
			self.txtDes.SetValue(self.desFold)
		dlg.Destroy()

	def showMessageBox(self, message, title):
		dlg = wx.MessageDialog(self, message, title, wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

#	def onCopy(self, event):
#		self.srcFile = self.txtSrc.GetValue();
#		logging.error(self.srcFile);
#		if(os.path.isfile(self.srcFile)==False):
#			msg = u'文件 ['+self.srcFile+u'] 不存在';
#			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
#			dlg.ShowModal()
#			dlg.Destory()
#			return;
#		
#		if(os.path.isfile(self.srcFile)==False):
#			msg = u'目录 ['+self.srcFile+u'] 不存在';
#			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
#			dlg.ShowModal()
#			dlg.Destory()
#			return;
#
#		#shutil.copy(self.srcFile, self.desFold)
#		print '...............................'
#		try:
#			print self.srcFile
#			tar = tarfile.open(self.srcFile)
#			names = tar.getnames()
#			for name in names:
#				tar.extract(name, self.desFold)
#			
#			tar.close()
#
#			#self.setSaHomeEnv(self.sa_home)
#
#			self.showMessageBox(u'安装完成', u'提示')
#		except ExtractError, e:
#			print "ExtractError e"
#			self.showMessageBox(u'tar包解压失败', u'错误')

	def onCopy(self, event):
		
		if(os.path.isdir(self.desFold)==False):
			msg = u'目录 ['+self.desFold+u'] 不存在';
			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
			dlg.ShowModal()
			dlg.Destory()
			return;

		self.logPanel.Clear()
		#shutil.copy(self.srcFile, self.desFold)
		self.CopyData(self.srcFile1, self.desFold)
		self.CopyData(self.srcFile2, self.desFold)
		self.CopyData(self.srcFile3, self.desFold)
		self.CopyData(self.srcFile4, self.desFold)

		self.showMessageBox(u'安装完成', u'提示')
		

	def CopyData(self, srcFile, targetDir):

		logging.error(srcFile)
		if(os.path.isfile(srcFile)==False):
			msg = u'文件 ['+ srcFile+u'] 不存在';
			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
			dlg.ShowModal()
			#dlg.Destory()
			return;

		self.logPanel.Append(u'解压文件[' + srcFile + ']\n')
		try:
			tar = tarfile.open(srcFile)
			names = tar.getnames()
			for name in names:
				self.logPanel.Append(name + '\n')
				tar.extract(name, targetDir)
			tar.close()
		except ExtractError, e:
			print e
			self.showMessageBox(u'tar包解压失败', u'错误')

	def SetLogPanel(self,logPanel):
		self.logPanel = logPanel


if __name__ == '__main__':
	app = wx.App(False)
	mainWin = FrmDataCopy(None)
	mainWin.Show(True)
	app.MainLoop()