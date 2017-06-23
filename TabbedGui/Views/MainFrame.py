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
        self.btnId = self.button.GetId()
        self.Bind(wx.EVT_BUTTON,self.OnButton,self.button)
        
    def OnButton(self,event):
        """ Called when the Button is clicked"""
        print("\nFrame GetChildren:")
        for child in self.GetChildren():
            print("%s" % repr(child))
        print("\nPanel FindWindowById")
        button = self.panel.FindWindowById(self.btnId)
        print("%s"%repr(button))
        button.SetLabel("Changed Label")
        print("\nButton GetParent:")
        panel = button.GetParent()
        print("%s"%repr(panel))
        print("\nGet the Application Object:")
        app = wx.GetApp()
        print("%s"%repr(app))
        print("\nGet the Frame from the App:")
        frame = app.GetTopWindow()
        print("%s"%repr(frame))
            
        