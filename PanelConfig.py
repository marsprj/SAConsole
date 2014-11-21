#coding=utf-8

import wx

class ConfigPanel(wx.Panel):
	def __init__(self, parent, ID=-1, label='', pos=wx.DefaultPosition, size=(100, 25)): 
		wx.Panel.__init__(self, parent, ID, pos, size, wx.NO_BORDER, label)

		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		btn = wx.Button(self, -1, u"control_variables_grid")
		self.Bind(wx.EVT_BUTTON, self.onControlVariablesGrid, btn)
		hbox1.Add(btn, flag=wx.RIGHT,border=0)
		btn = wx.Button(self, -1, u"shapefile_catalog")		
		self.Bind(wx.EVT_BUTTON, self.onShapefileCatalog, btn)
		hbox1.Add(btn, flag=wx.RIGHT,border=0)
		btn = wx.Button(self, -1, u"surrogate_codes")		
		hbox1.Add(btn, flag=wx.RIGHT,border=0)
		btn = wx.Button(self, -1, u"surrogate_generation_grid")		
		hbox1.Add(btn, flag=wx.RIGHT,border=0)
		btn = wx.Button(self, -1, u"surrogate_specification_2002")		
		hbox1.Add(btn, flag=wx.RIGHT,border=0)
		btn = wx.Button(self, -1, u"GRIDDESC")
		hbox1.Add(btn, flag=wx.RIGHT,border=0)

		vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=0)
		vbox.Add((-1,5))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.content = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		hbox3.Add(self.content, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=0)

		self.SetSizer(vbox)

	def onControlVariablesGrid(self, event):
		self.fpath = 'G:\\temp\\Map.js'
		try:
			fp = open(self.fpath)
			text = fp.read()
			self.content.SetValue(text)
		finally:
			fp.close()

	def onShapefileCatalog(self, event):
		self.fpath = 'G:\\temp\\wms.xml'
		try:
			fp = open(self.fpath)
			text = fp.read()
			self.content.SetValue(text)
		except Exception as err: 
			print err
		finally:
			fp.close()

	def onSave():
		text = self.content.GetValue()
		try:
			fp = open(self.fpath,'w')
			fp.write(text)
		finally:
			fp.close();

