#coding=utf-8

import wx
import logging

class FrmMain(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, title=u'SA管理控制台', size=(600,100),style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX))

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

		self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		#self.content = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
		#hbox3.Add(self.content, proportion=1, flag=wx.EXPAND)
		self.p1 = wx.Panel(panel)
		self.p1.SetBackgroundColour('Red') 
		self.hbox3.Add(self.p1, proportion=1, flag=wx.EXPAND)
		self.p2 = wx.Panel(panel)
		self.p2.SetBackgroundColour('Blue') 
		self.p2.Show(False)
		self.hbox3.Add(self.p2, proportion=1, flag=wx.EXPAND)
		self.hbox3.Layout()
		vbox.Add(self.hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=3)

		panel.SetSizer(vbox)

	def onInstall(self, event):
		pass

	def onCopyData(self, event):
		pass

	def onConfiguration(self, event):
		pass

	def onRun(self, event):
		pass

	def onResult(self, event):
		pass

	def onLog(self, event):
		pass

if __name__ == '__main__':
	app = wx.App()
	frmMain = FrmMain(None)
	frmMain.Show(True)
	frmMain.Maximize(True)
	frmMain.Centre()
	app.MainLoop()