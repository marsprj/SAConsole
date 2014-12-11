#coding=utf-8

import wx
import os
import sys
import logging
import SAConfig
from RunThread import RunThread

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
		self.sa_name = SAConfig.GetValue('sa_name')
		self.sa_base = os.path.join(self.sa_home, self.sa_name)
		self.sa_dir  = os.path.join(self.sa_base, 'srgtools')
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
		self.Bind(wx.EVT_BUTTON, self.OnRun, btn)
		hbox1.Add(btn, flag=wx.LEFT|wx.RIGHT,border=10)

		btn = wx.Button(self, -1, u"日志")
		self.Bind(wx.EVT_BUTTON, self.onReadLog, btn)
		hbox1.Add(btn, flag=wx.LEFT|wx.RIGHT,border=10)

		vbox.Add((-1,10))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.txtLog = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_MULTILINE)
		self.txtLog.SetBackgroundColour('#FFFFFF')
		hbox3.Add(self.txtLog, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

		vbox.Add((-1, 25))
		self.SetSizer(vbox)
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.onReadLog, self.timer)

	def OnRun(self, event):
		
		#os.remove(self.sa_log)		

		self.timer.Start(3*1000)
		exe_cmd  = 'java -classpath ' + self.sa_exe + ' gov.epa.surrogate.SurrogateTool control_variables_grid.csv'
		exe_cmd  = 'cd ' + self.sa_dir  + ';java -classpath SurrogateTools.jar gov.epa.surrogate.SurrogateTool control_variables_grid.csv'
		#print exe_cmd
		#os.popen(exe_cmd)
		#self.timer.Stop()

		self.thread = RunThread(exe_cmd, self)
		self.thread.start()

	def OnLog(self, event):
		self.timer.Stop()

	def onReadLog(self, event):
		#print '[log path]:' + self.sa_log +'\n'
		fp = None
		try:
			fp = open(self.sa_log)
			text = fp.read()
			self.txtLog.SetValue(text)
			pos = self.txtLog.XYToPosition(0,self.txtLog.GetNumberOfLines()-1)
			self.txtLog.ShowPosition(pos)
		except IOError,e:
			logging.error(e)
		finally:
			if(fp!=None):
				fp.close()

	def OnRunFinish(self, message):
		self.timer.Stop()

		dlg = wx.MessageDialog(self, u'运行结束', u'提示', wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
	

	def WriteLog(self, message):
		pass

	def GetOutputSubDir(self):
		pass
