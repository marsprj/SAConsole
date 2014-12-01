#coding=utf-8

import wx
import os
import shutil
import tarfile
import SAConfig
from UntarThread import UntarThread


class FrmCopyFolder(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title=u'数据部署',size=(460,300),style=(wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR)^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))

		self.parent = parent
		self.untar_thread = None

		panel = wx.Panel(self)

		self.des_dir = SAConfig.GetValue('sa_home')
		self.src_dir = SAConfig.GetValue('sa_home')

		wx.StaticText(panel,label=u'目标目录:', pos=(20,20))
		self.txtDesFolder = wx.TextCtrl(panel, pos=(90,18), size=(300,25), style=wx.TE_READONLY)
		self.txtDesFolder.SetBackgroundColour('#FFFFFF')
		bmp =  wx.Image('images/folder_24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		#btnSrcFolder = wx.Button(panel, label=u'数据目录', pos=(400,15), size=(80,30))
		btnDesFolder = wx.BitmapButton(panel, id=-1, pos=(400,15), bitmap=bmp, size=wx.DefaultSize, style=wx.BU_AUTODRAW, validator=wx.DefaultValidator, name=u'数据目录')
		self.Bind(wx.EVT_BUTTON, self.onSelectDesFolder, btnDesFolder)

		wx.StaticText(panel,label=u'数据目录:', pos=(20,58))
		#btnSrcFolder = wx.Button(panel,label=u'选择目录', pos=(400,55), size=(80,30))
		btnSrcFolder = wx.BitmapButton(panel, id=-1, pos=(400,55), bitmap=bmp, size=wx.DefaultSize, style=wx.BU_AUTODRAW, validator=wx.DefaultValidator, name=u'选择目录')	
		self.Bind(wx.EVT_BUTTON, self.onSelectSrcFolder, btnSrcFolder)

		bmp =  wx.Image('images/copy_24.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		#btnSrcFolder = wx.Button(panel,label=u'复制数据', pos=(400,100), size=(80,80))
		btnSrcFolder = wx.BitmapButton(panel, id=-1, pos=(400,100), bitmap=bmp, size=wx.DefaultSize, style=wx.BU_AUTODRAW, validator=wx.DefaultValidator, name=u'选择目录')	
		self.Bind(wx.EVT_BUTTON, self.OnCopyData, btnSrcFolder)

		self.list = wx.ListCtrl(panel, pos=(90,60), size=(300, 200), style=wx.LC_REPORT)
		self.list.InsertColumn(0, u'路径')
		self.list.SetColumnWidth(0,300)

	def onSelectDesFolder(self, event):
		dlg = wx.DirDialog(self, u'选择安装路径',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			self.des_dir = dlg.GetPath()
			self.txtDesFolder.SetValue(self.des_dir)
		dlg.Destroy()

	def onSelectSrcFolder(self, event):
		dlg = wx.DirDialog(self, u'选择安装路径',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			src_dir = dlg.GetPath()
			self.list.InsertStringItem(0, src_dir)
			print self.list.GetItemCount()
		dlg.Destroy()

	def OnCopyData(self, event):
		des_dir = self.des_dir
		count = self.list.GetItemCount()
		for i in range(0,count):
			src_folder = self.list.GetItemText(i)
			des_folder = os.path.join(des_dir, os.path.basename(src_folder))
			self.CopyFolder(src_folder, des_folder)			
			print des_folder
		self.ShowMessageBox(u'完成数据部署',u'提示')	

	def CopyFolder(self, src, des):
	
		#print '[src]:' + src
		# check whether tar file exists
		if(os.path.isdir(src)==False):
			self.ShowMessageBox(u'数据目录['+src+u']不存在', u'警告')
			return;

		if(os.path.isdir(des)==False):
			self.ShowMessageBox(u'目录 ['+des+u'] 不存在', u'警告')
			return;

		self.logPanel.Append(u'复制目录[' + src + ']\n')
		shutil.copytree(src, des)


	def ShowMessageBox(self, message, title):
		dlg = wx.MessageDialog(self, message, title, wx.OK)
		dlg.ShowModal()
		dlg.Destroy()


	def SetLogPanel(self,logPanel):
		self.logPanel = logPanel
