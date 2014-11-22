#coding=utf-8

import wx
import os
import sys
import logging
import SAConfig

class RedirectText(object):
	def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl

	def write(self,string):
		self.out.WriteText(string)

class RunPanel(wx.Panel):

	def __init__(self, parent, ID=-1, label=u'SA运行程序', pos=wx.DefaultPosition, size=(100, 25)): 
		wx.Panel.__init__(self, parent, ID, pos, size, wx.NO_BORDER, label)
		self.initUI()

	def initUI(self):

		self.sa_home = SAConfig.GetValue('sa_home')
		self.sa_dir  = self.sa_home
		self.sa_exe  = os.path.join(self.sa_dir, 'SurrogateTools.jar')
		self.sa_log  = os.path.join(self.sa_dir, 'srg_grid.log')
		
		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(self,label=u'程序')
		#st1.SetFont(font)

		hbox1.Add(st1,flag=wx.RIGHT,border=8)
		txtPath = wx.TextCtrl(self,style=wx.TE_READONLY)
		txtPath.SetBackgroundColour('#FFFFFF')
		txtPath.SetValue(self.sa_exe)
		hbox1.Add(txtPath,proportion=1)		
		vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		btn = wx.Button(self, -1, u"运行")
		self.Bind(wx.EVT_BUTTON, self.onRun, btn)
		hbox1.Add(btn, flag=wx.LEFT|wx.RIGHT,border=10)

		btn = wx.Button(self, -1, u"日志")
		self.Bind(wx.EVT_BUTTON, self.onLog, btn)
		hbox1.Add(btn, flag=wx.LEFT|wx.RIGHT,border=10)

		vbox.Add((-1,10))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.txtLog = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_MULTILINE)
		self.txtLog.SetBackgroundColour('#FFFFFF')
		hbox3.Add(self.txtLog, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

		vbox.Add((-1, 25))
		self.SetSizer(vbox)

	def onRun(self, event):		
		logging.error('onRun.....')
		#sys.stdout = RedirectText(self.txtLog) 
		exe_cmd  = 'java -classpath ' + self.sa_exe + ' gov.epa.surrogate.SurrogateTool control_variables_grid.csv'
		logs = os.system(exe_cmd)
		#logs = os.popen(exe_cmd).readlines()
		#print logs

	def onLog(self, event):		
		fp = None
		try:
			fp = open(self.sa_log)
			text = fp.read()
			self.txtLog.SetValue(text)
		except IOError,e:
			logging.error(e)
		finally:
			if(fp!=None):
				fp.close()

