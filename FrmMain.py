#coding=utf-8

import wx
import logging
#from InstallDialog import InstallDialog
from PanelConfig import ConfigPanel
from PanelRun import RunPanel
from PanelResult import ResultPanel
from PanelLog import LogPanel
from FrmInstall import FrmInstall
from FrmDataCopy import FrmDataCopy

class FrmMain(wx.Frame):
	def __init__(self, parent):
		#wx.Frame.__init__(self, parent, title=u'SA管理控制台', size=(600,600),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))
		wx.Frame.__init__(self, parent, title=u'SA管理控制台', size=(600,600))

		panel = wx.Panel(self)

		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox_bar = wx.BoxSizer(wx.HORIZONTAL)
		#u'安装'
		bmp =  wx.Image('images/01.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, id=-1, bitmap=bmp, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.BU_AUTODRAW, validator=wx.DefaultValidator, name=u'安装')
		self.Bind(wx.EVT_BUTTON, self.onInstall, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND)
		#u"拷贝数据"
		bmp =  wx.Image('images/02.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, -1, bmp)
		self.Bind(wx.EVT_BUTTON, self.onCopyData, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND)		
		#u"配置文件"
		bmp =  wx.Image('images/03.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, -1, bmp)
		self.Bind(wx.EVT_BUTTON, self.onConfiguration, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND,border=10)
		#u"运行程序"
		bmp =  wx.Image('images/04.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, -1, bmp)
		self.Bind(wx.EVT_BUTTON, self.onRun, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND)
		#u"运行结果"
		bmp =  wx.Image('images/05.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, -1, bmp)
		self.Bind(wx.EVT_BUTTON, self.onResult, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND)
		#u"查看日志"
		bmp =  wx.Image('images/06.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		btn = wx.BitmapButton(panel, -1, bmp)
		self.Bind(wx.EVT_BUTTON, self.onLog, btn)
		hbox_bar.Add(btn, 1, wx.EXPAND)

 		vbox.Add(hbox_bar,flag=wx.LEFT|wx.RIGHT|wx.TOP,border=3)
		vbox.Add((-1,5))

#		self.hbox_main = wx.BoxSizer(wx.HORIZONTAL)
#		self.p1 = wx.Panel(panel)
#		self.p1.SetBackgroundColour('Red') 
#		self.hbox_main.Add(self.p1, proportion=1, flag=wx.EXPAND)
#		# Config Panel
#		self.panenConfig = ConfigPanel(panel)
#		self.panenConfig.Show(False)
#		self.hbox_main.Add(self.panenConfig, proportion=1, flag=wx.EXPAND)
#		self.hbox_main.Layout()
#		vbox.Add(self.hbox_main, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=3)

		self.hbox_main = wx.BoxSizer(wx.HORIZONTAL)
		self.InitPanels(panel, self.hbox_main)
		self.ShowPanel(0)
		vbox.Add(self.hbox_main, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=3)

		panel.SetSizer(vbox)

	def onInstall(self, event):

		self.ShowPanel(1)

		frm = FrmInstall(self)
		frm.SetLogPanel(self.GetPanel(0))
		frm.Centre()
		frm.Show(True)
#		dlg = InstallDialog()
#		dlg.Centre()
#		result = dlg.ShowModal()
#		if result == wx.ID_OK:
#			print 'OK'
#		else:
#			print 'Cancel'
#		dlg.Destroy()

	def onCopyData(self, event):
		self.ShowPanel(1)
		#self.ShowPanel(1)
		frm = FrmDataCopy(self)
		frm.SetLogPanel(self.GetPanel(1))
		frm.Centre()
		frm.Show(True)

	def onConfiguration(self, event):
		self.ShowPanel(2)

	def onRun(self, event):
		print 'onRun'
		self.ShowPanel(3)

	def onResult(self, event):
		p = self.GetPanel(4)
		p.UpdateTree()
		self.ShowPanel(4)

	def onLog(self, event):
		self.ShowPanel(5)

	def InitPanels(self, parent, hbox):
		#p1 = wx.Panel(parent)
		p1 = LogPanel(parent)
		p2 = LogPanel(parent)
		p3 = ConfigPanel(parent)
		p4 = RunPanel(parent)
		p5 = ResultPanel(parent)
		self.panels = [p1,p2, p3, p4, p5]
		for p in self.panels:
			if(p!=None):
				hbox.Add(p, proportion=1, flag=wx.EXPAND)
				p.Show(False)

	def ShowPanel(self, index):
		for p in self.panels:
			if(p!=None):
				p.Show(False)
		print len(self.panels)
		if(index<len(self.panels)):
			p = self.panels[index]
			if(p!=None):
				p.Show(True)
				self.hbox_main.Layout()

	def GetPanel(self, index):
		print len(self.panels)
		if(index<len(self.panels)):
			return self.panels[index]
		return None
