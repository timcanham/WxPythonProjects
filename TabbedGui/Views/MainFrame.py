import wx

class MainFrame(wx.Frame):
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,title="",
                 pos = wx.DefaultPosition,
                 size = wx.DefaultSize,
                 style = wx.DEFAULT_FRAME_STYLE,
                 name = "MainFrame"):
        super(MainFrame,self).__init__(parent, id, title, pos, size, style, name)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLACK)
        self.button = wx.Button(self.panel,label="Push Me",pos=(50,50))