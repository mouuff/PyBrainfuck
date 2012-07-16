from sys import stdout, argv

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
	
	def __repr__(self):
		return self.script
	
	def __getitem__(self, x):
		return self.table[x]
	
	def __setitem__(self, x, y):
		self.table[x] = y
	
	def reset(self):
		self.__init__()
	
	def autorun(self, script):
		'''Auto run the BF script
		Beta options...'''
		self.load(script)
		self.clean()
		self.check()
		try:
			return self.run()
		except (MemoryError):
			print("RAM error")
			return 1
	
	def load(self, script):
		'''Load a script, this is requiered'''
		self.script = script
	
	def add(self, part):
		'''Add code to the script'''
		for char in part:
			if (char in '+-<>.,[]#'):
				self.script += char
	
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
		str(self.script)#try if the script is type of string
		if (self.script.count("[") != self.script.count("]")):
			raise SyntaxError
		if (self.script.find("[]") != -1):
			raise SyntaxError
			
	def run(self):
		'''Run the loaded script,
		use .load() before'''
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
						stdout.write(chr(self.table[self.pointer]))
					except (ValueError):
						pass
					stdout.flush()
					
				elif (self.script[self.progress] == ','):
					self.table[self.pointer] = ord(raw_input())
					
				elif (self.script[self.progress] == '['):
					self.loop += 1
				
				elif (self.script[self.progress] == '#'):
					print list(set(self.table))
				
				elif (self.loop):
					if (self.script[self.progress] == ']'):
						if (self.table[self.pointer] > 0):
							self.progress = self.script.find('[')
						else:
							self.loop -= 1
							if (not self.loop):
								self.progress = 0
								self.script = self.script[self.script.find("]")+1:]
			self.progress += 1
		return list(set(self.table))


if __name__ == '__main__':
	try:
		bf = pybf()
		bf.load(open(argv[1]).read())
		bf.run()
	except (IOError, IndexError):
		print("WB in PyBrainf***")
		print("Error, file not found or arguements error\nprint switching to console.[Press enter to launch the script]")
		bf = pybf()
		while (True):
			command = raw_input("& ")
			if (len(command)):
				bf.add(command)
			else:
				print bf.run()
				bf = pybf()
