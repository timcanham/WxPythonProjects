import wx
from Views import MainFrame

class MainApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame.MainFrame(None,
           title = "Main Frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True