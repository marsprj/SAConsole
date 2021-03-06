#coding=utf-8

import wx
import os
import logging
import SAConfig

class LogPanel(wx.Panel):
	def __init__(self, parent, ID=-1, label='', pos=wx.DefaultPosition, size=(100, 25)): 
		wx.Panel.__init__(self, parent, ID, pos, size, wx.NO_BORDER, label)

		self.config_path = ''
		self.config_dir = os.path.join(SAConfig.GetValue('sa_home'), 'conf')

		vbox = wx.BoxSizer(wx.VERTICAL)
		
		self.logCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)
		vbox.Add(self.logCtrl, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=3)

		self.SetSizer(vbox)

	def SetText(self, text):
		self.logCtrl.SetValue(text)

	def Append(self, text):
		self.logCtrl.AppendText(text)
		self.logCtrl.AppendText('\n')
		logging.info(text)

	def AppendTexts(self, texts):
		for t in texts:
			self.logCtrl.AppendText(t)

	def Clear(self):
		self.logCtrl.Clear()
