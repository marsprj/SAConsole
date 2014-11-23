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

	def OnControlVariablesGrid(self, event):
		self.config_path = self.buildConconfig_path("control_variables_grid.csv")
		self.OpenConfig(self.config_path)

	def OnShapefileCatalog(self, event):
		self.config_path = self.buildConconfig_path("shapefile_catalog.csv")
		self.OpenConfig(self.config_path)

	def OnSurrogateCodes(self, event):
		self.config_path = self.buildConconfig_path("surrogate_codes.csv")
		self.OpenConfig(self.config_path)

	def OnSurrogateGenerationGrid(self, event):
		self.config_path = self.buildConconfig_path("surrogate_generation_grid.csv")
		self.OpenConfig(self.config_path)

	def OnSurrogateSpecification2002(self, event):
		self.config_path = self.buildConconfig_path("surrogate_specification_2002.csv")
		self.OpenConfig(self.config_path)

	def OnGridDesc(self, event):
		self.config_path = self.buildConconfig_path("GRIDDESC.txt")
		self.OpenConfig(self.config_path)


	def OpenConfig(self, config_path):
		fp = None
		try:
			fp = open(config_path)
			text = fp.read()
			self.logCtrl.SetValue(text)
		except IOError,e:
			logging.error(e)
		finally:
			if(fp!=None):
				fp.close()

	def OnSave(self, event):
		text = self.logCtrl.GetValue()
		fp = None
		try:
			fp = open(self.config_path,'w')
			fp.write(text)
			self.showMessageBox(u'保存成功',u'提示')
		except IOError,e:
			logging.error(e)
		finally:
			if(fp!=None):
				fp.close();

	def KeyPress(self, evt):
		if(evt.GetKeyCode()==19):	# Ctrl+S
			text = self.logCtrl.GetValue()
			fp = open(self.config_path,'w')
			try:
				fp.write(text)
				self.showMessageBox(u'保存成功',u'提示')			
			finally:
				fp.close();
		

	def buildConconfig_path(self, conf_name):
		return os.path.join(self.config_dir, conf_name)

	def showMessageBox(self, message, title):
		dlg = wx.MessageDialog(self, message, title, wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def Append(self, text):
		self.logCtrl.AppendText(text)

	def Clear(self):
		self.logCtrl.Clear()