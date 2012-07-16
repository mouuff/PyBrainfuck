#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

__all__ = ('pybf')
__doc__ = ('''
PyBF
A tiny and bugged brainfuck interpreter
''')
__version__ = "1.0"

class pybf:
	def __init__(self):
		'''Brainfuck interpreter'''
		self.table = [0]*3000
		self.pointer = 0
		self.progress = 0
		self.loop = 0
		self.script = ''

	
	def load(self, script):
		'''Load a script, this is requiered'''
		self.script = script
	
	def add(self, part):
		'''Add code to the script'''
		self.script += part
	
	def clean(self):
		'''option to clean script to speed up big scripts'''
		script = ''
		removed = 0
		for char in self.script:
			if (char in '+-<>.,[]#'):
				script += char
			else:
				removed += 1
		self.script = script
		return removed

	def check(self):
		'''Check if any errors, not complete yet.'''
		if (self.script.count("[") != self.script.count("]")):
			raise SyntaxError
		if (self.script.find("[]") != -1):
			raise SyntaxError
		
			
	def execute(self, xinput=""):
		out= 'Output:\n'
		placement = 0
		while (self.progress < len(self.script)):
			if (self.script[self.progress] in '+-<>.,[]#'):
				if (self.script[self.progress] == '+'):
					self.table[self.pointer] += 1
					
				elif (self.script[self.progress] == '-'):
					if (self.table[self.pointer] > 0):
						self.table[self.pointer] -= 1
					
				elif (self.script[self.progress] == '>'):
					self.pointer += 1
					
				elif (self.script[self.progress] == '<'):
					if (self.pointer > 0):
						self.pointer -= 1
					
				elif (self.script[self.progress] == '.'):
					try:
						out += chr(self.table[self.pointer])
					except (ValueError):
						out += '?'
					
				elif (self.script[self.progress] == ','):
					if (placement < len(xinput)):
						self.table[self.pointer] = ord(xinput[placement])
						placement += 1

					
				elif (self.script[self.progress] == '['):
					self.loop += 1
				
				elif (self.script[self.progress] == '#'):
					out +=  str(list(set(self.table)))
				
				elif (self.loop):
					if (self.script[self.progress] == ']'):
						if self.table[self.pointer] > 0:
							self.progress = self.script.find('[')
						else:
							self.loop -= 1
							if (not self.loop):
								self.progress = 0
								self.script = self.script[self.script.find("]")+1:]
			self.progress += 1
		return out


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.label_1 = wx.StaticText(self, -1, "Enter code below:")
		self.label_2 = wx.StaticText(self, -1, "Script:")
		self.script = wx.TextCtrl(self, -1, "")
		self.label_3 = wx.StaticText(self, -1, "Pre-input:")
		self.preinput = wx.TextCtrl(self, -1, "")
		self.output = wx.StaticText(self, -1, "Output: ")
		self.compile = wx.Button(self, -1, "OK")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_TEXT_ENTER, self.xscript, self.script)
		self.Bind(wx.EVT_TEXT_ENTER, self.xpreinput, self.preinput)
		self.Bind(wx.EVT_BUTTON, self.start, self.compile)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("Pybrainfuck")
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(1, 2, 0, 0)
		grid_sizer_5 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_2 = wx.GridSizer(3, 1, 0, 0)
		grid_sizer_4 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_3 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_2.Add(self.label_1, 0, wx.EXPAND, 0)
		grid_sizer_3.Add(self.label_2, 0, wx.EXPAND, 0)
		grid_sizer_3.Add(self.script, 0, wx.EXPAND, 0)
		grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
		grid_sizer_4.Add(self.label_3, 0, wx.EXPAND, 0)
		grid_sizer_4.Add(self.preinput, 0, wx.EXPAND, 0)
		grid_sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
		grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		grid_sizer_5.Add(self.output, 0, 0, 0)
		grid_sizer_5.Add(self.compile, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)
		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

	def xscript(self, event):
		event.Skip()

	def xpreinput(self, event):
		event.Skip()

	def start(self, event): # wxGlade: MyFrame.<event_handler>
		compiler = pybf()
		compiler.load(self.script.GetValue())
		self.output.SetLabel(compiler.execute(self.preinput.GetValue()))
		event.Skip()

# end of class MyFrame


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
