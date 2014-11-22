#coding=utf-8

import wx;
import os;
import shutil;
import logging;

class FrmDataCopy(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title=u'拷贝数据',size=(500,170),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))

		panel = wx.Panel(self)

		self.srcFile = '';
		self.desFold = 'g://temp';

		# Choose Source File
		wx.StaticText(panel, label=u'数据文件:', pos=(20,20))
		self.txtSrc = wx.TextCtrl(panel, pos=(90,18), size=(300,25), style=wx.TE_READONLY)
		self.txtSrc.SetBackgroundColour('#FFFFFF')
		btnSrc = wx.Button(panel, label=u'选择文件', pos=(400,15), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChoosFile, btnSrc)
		self.txtSrc.SetValue(self.srcFile);

		# Choose Target Folder
		wx.StaticText(panel, label=u'目标路径:', pos=(20,58))
		self.txtDes = wx.TextCtrl(panel, pos=(90,58), size=(300,25), style=wx.TE_READONLY)
		self.txtDes.SetBackgroundColour('#FFFFFF')
		btnDes = wx.Button(panel, label=u'目标路径', pos=(400,55), size=(80,30))
		self.Bind(wx.EVT_BUTTON, self.onChooseDestination, btnDes)
		self.txtDes.SetValue(self.desFold);

		# Copy Button
		btnCopy = wx.Button(panel, label=u'拷贝数据', pos=(180,100), size=(120,30))
		self.Bind(wx.EVT_BUTTON, self.onCopy, btnCopy)


	def onChoosFile(self, event):
		dlg = wx.FileDialog(self, u'选择数据文件', self.srcFile, '', '*.*', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.srcFile = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			self.txtSrc.SetValue(self.srcFile)
		dlg.Destroy()

	def onChooseDestination(self, event):
		dlg = wx.FileDialog(self, u'选择路径', self.desFold, '', '*.*', wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.desFold = dlg.GetDirectory()			
			self.txtDes.SetValue(self.desFold)
		dlg.Destroy()

	def onCopy(self, event):
		self.srcFile = self.txtSrc.GetValue();
		logging.error(self.srcFile);
		if(os.path.isfile(self.srcFile)==False):
			msg = u'文件 ['+self.srcFile+u'] 不存在';
			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
			dlg.ShowModal()
			dlg.Destory()
			return;
		
		if(os.path.isfile(self.srcFile)==False):
			msg = u'目录 ['+self.srcFile+u'] 不存在';
			dlg = wx.MessageDialog( self, msg, u'警告', wx.OK)
			dlg.ShowModal()
			dlg.Destory()
			return;

		shutil.copy(self.srcFile, self.desFold)

if __name__ == '__main__':
	app = wx.App(False)
	mainWin = FrmDataCopy(None)
	mainWin.Show(True)
	app.MainLoop()