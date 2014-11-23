#coding=utf-8

import wx
import os
import sys
import logging
import SAConfig

class ResultPanel(wx.Panel):

	def __init__(self, parent, ID=-1, label=u'运行结果', pos=wx.DefaultPosition, size=(100, 25)): 
		wx.Panel.__init__(self, parent, ID, pos, size, wx.NO_BORDER, label)
		self.initUI()

	def initUI(self):

		self.sa_home = SAConfig.GetValue('sa_home')
		self.sa_out  = os.path.join(self.sa_home, 'output/somegrid')
		#self.sa_out  = 'g:\\'
		#self.sa_out  = 'G:\\Software\\Tool'
		#self.sa_out  = 'E:\\Research\\SAConsole\\v-0.0.3'
		#self.sa_out  = 'G:\\temp'
		
		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(self,label=u'运行结果路径')
		#st1.SetFont(font)

		hbox1.Add(st1,flag=wx.RIGHT,border=8)
		txtPath = wx.TextCtrl(self,style=wx.TE_READONLY)
		txtPath.SetBackgroundColour('#FFFFFF')
		txtPath.SetValue(self.sa_out)
		hbox1.Add(txtPath,proportion=1)		
		vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		btn = wx.Button(self, -1, u"刷新")
		self.Bind(wx.EVT_BUTTON, self.OnRefresh, btn)
		hbox1.Add(btn, flag=wx.LEFT|wx.RIGHT,border=10)

		vbox.Add((-1,10))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)

		self.treeCtrl = wx.TreeCtrl(self, -1, style=wx.TR_HAS_BUTTONS|wx.TR_DEFAULT_STYLE|wx.SUNKEN_BORDER)
		self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivated, self.treeCtrl)
		self.InitTree(self.treeCtrl)		
		hbox3.Add(self.treeCtrl, proportion=1, flag=wx.EXPAND)

		self.contentCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		hbox3.Add(self.contentCtrl,proportion=4, flag=wx.EXPAND)	
		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

		vbox.Add((-1, 25))
		self.SetSizer(vbox)
		
	def InitTree(self, treeCtrl):
		il = wx.ImageList(16,16)
		il.Add(wx.Bitmap('images/folder.png', wx.BITMAP_TYPE_PNG))
		il.Add(wx.Bitmap('images/file_white.png', wx.BITMAP_TYPE_PNG))
		treeCtrl.AssignImageList(il)

		self.treeRoot = treeCtrl.AddRoot(u'输出数据')
		treeCtrl.SetItemImage(self.treeRoot, 0, wx.TreeItemIcon_Normal)

		self.UpdateTreeNode(self.treeRoot, self.sa_out)

		treeCtrl.ExpandAll()


	def UpdateTreeNode(self, tnode, path):
		self.treeCtrl.DeleteChildren(tnode)
		files = os.listdir(path)
		for fn in files:
			fp = os.path.join(path, fn)
			tn = self.treeCtrl.AppendItem(tnode, fn)
			#self.treeCtrl.SetItemData(tn, fp)
			if(os.path.isdir(fp)):
				self.treeCtrl.SetItemImage(tn, 0, wx.TreeItemIcon_Normal)
			else:
				self.treeCtrl.SetItemImage(tn, 1, wx.TreeItemIcon_Normal)

	def OnRefresh(self, event):
		pass

	def OnActivated(self, event):
		item = event.GetItem()
		fname = self.treeCtrl.GetItemText(item)
		fpath = os.path.join(self.sa_out, fname)
		if(os.path.isfile(fpath)):
			(fdir,fext) = os.path.splitext(fpath)
			if((fext=='.txt')|(fext=='.xml')):
				fp = None
				try:
					fp = open(fpath)
					text = fp.read()
					self.contentCtrl.SetValue(text)
					pass
				except IOError, e:
					logging.error(e)
					raise
				else:
					pass
				finally:
					if(fp!=None):
						fp.close()


	

