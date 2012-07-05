#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

def BF(script):
	''''Launch a Brainfuck script'''
	table = [0]*3000
	pointer = 0
	progress = 0
	out = ''
	loop = 0
	while (progress < len(script)):
		if (script[progress] in '+-<>.,[]'):
			if (script[progress] == '+'):
				table[pointer] += 1
				
			elif (script[progress] == '-'):
				table[pointer] -= 1
				
			elif (script[progress] == '>'):
				pointer += 1
				
			elif (script[progress] == '<'):
				pointer -= 1
				
			elif (script[progress] == '.'):
				try:
					out += (chr(table[pointer]))
				except (ValueError):
					out += '?'
				
			elif (script[progress] == ','):
				table[pointer] = ord(raw_input())
				
			elif (script[progress] == '['):
				loop += 1
				
			elif (loop):
				if (script[progress] == ']'):
					if table[pointer] > 0:
						progress = script.find('[')
					else:
						loop -= 1
		progress += 1
	return out


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_2 = wx.StaticText(self, -1, "PyBrainFuu")
        self.label_3 = wx.StaticText(self, -1, "Enter some BF code:")
        self.xinput = wx.TextCtrl(self, -1, "")
        self.button_1 = wx.Button(self, -1, "OK")
        self.output = wx.StaticText(self, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.oninput, self.xinput)
        self.Bind(wx.EVT_BUTTON, self.out, self.button_1)

    def __set_properties(self):
        self.SetTitle("Brainfuck interpreter")

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2.Add(self.label_2, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_2.Add(self.label_3, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.xinput, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.output, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

    def oninput(self, event):
        event.Skip()

    def out(self, event):
        self.output.SetLabel(BF(self.xinput.GetValue()))
        event.Skip()



if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
