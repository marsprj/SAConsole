#coding=utf-8

import wx
from FrmMain import FrmMain

class SApp(wx.App):
	def OnInit(self):
		#bmp = wx.Image("images/Hydrangeas.jpg").ConvertToBitmap()
		#wx.SplashScreen(bmp,
		#				wx.SPLASH_CENTER_ON_SCREEN | wx.SPLASH_TIMEOUT,
		#				1000,
		#				None,
		#				-1)
		#wx.Yield()
		frmMain = FrmMain(None)  
		frmMain.Show(True) 
		frmMain.Centre()
		frmMain.Maximize(True)
		self.SetTopWindow(frmMain)  
		return True


if __name__ == '__main__':
	app = SApp()
	app.MainLoop()