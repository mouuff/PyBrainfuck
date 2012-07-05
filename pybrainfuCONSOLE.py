from sys import stdout, argv

__all__ = ('BF')

class pybf:
	def __init__(self):
		'''Brainfuck interpreter'''
		self.table = [0]*30000
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
		for char in self.script:
			if (char in '+-<>.,[]'):
				script += char
		self.script = script

	def check(self):
		'''Check if any errors'''
		if (self.script.count("[") != self.script.count("]")):
			raise SyntaxError
			
	def execute(self):
		while (self.progress < len(self.script)):
			if (self.script[self.progress] in '+-<>.,[]'):
				if (self.script[self.progress] == '+'):
					self.table[self.pointer] += 1
					
				elif (self.script[self.progress] == '-'):
					if self.table[self.pointer] > 0:
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
						stdout.write('?')
					stdout.flush()
					
				elif (self.script[self.progress] == ','):
					self.table[self.pointer] = ord(raw_input())
					
				elif (self.script[self.progress] == '['):
					self.loop += 1
				
				elif (self.script[self.progress] == '#'):
					print self.table
				
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
		return list(set(self.table))

if __name__ == '__main__':
	try:
		bf = pybf()
		bf.load(open(argv[1]).read())
		bf.check()
		bf.execute()
	except (IOError, IndexError):
		print("Error, file not found or arguements error\nprint switching to console.[Press enter to launch the script]")
		bf = pybf()
		while (True):
			try:
				entre = raw_input("> ")
			except (EOFError, KeyboardInterrupt):
				break
			if (entre == ''):
				print("Launching script\n")
				try:
					bf.check()
				except SyntaxError:
					print("Failled to check, syntax error")
				print bf.execute()
				bf = pybf()
			else:
				bf.add(entre)
