from sys import stdout, argv

#a simple and working bf interpreter

class BF:
	def __init__(self):
		self.script = "" #bf script
		self.pointer = 0 #bf pointer
		self.progress = 0 #progress in the script
		self.Size = 50 #size of the array it will change when needed (check in run function)
		self.array = [0]*self.Size #default array
		
	def __repr__(self):
		return self.array
		
	def __getitem__(self, a):
		return self.array[a]
	
	def __setitem__(self, x, y):
		self.array[x] = y
		
	def add(self,string):
		self.script+=string
	
	def load(self,script):
		for x in script:
			if (x in "[]<>.,+-#"):
				self.script += x
	
	def run(self):
		while (self.progress < len(self.script)):
			char = self.script[self.progress]
			
			if (char=="+"):
				self.array[self.pointer] += 1
				
			elif (char=="-" and self.array[self.pointer] > 0):
				self.array[self.pointer] -= 1
					
			elif (char==">"):
				if (self.pointer<self.Size):
					self.Size+=50
					self.array+=[0]*50
				self.pointer += 1
				
			elif (char=="<" and self.pointer>0):
				self.pointer -= 1
				
			elif (char=="]" and self.array[self.pointer]):
				loops = 1
				while (loops >= 1):
					self.progress -= 1
					if (self.script[self.progress] == "]"):
						loops += 1
					if (self.script[self.progress] == "["):
						loops -= 1
						
			elif (char==","):
				self.table[self.pointer] = ord(raw_input())
			elif (char=="."):
				try:
					stdout.write(chr(self.array[self.pointer]))
				except (ValueError):
					pass
				stdout.flush()
			
			elif (char=="#"):
				print list(self.array)
				
			self.progress += 1


if (__name__=="__main__"):
	try:
		bf = BF()
		bf.load(open(argv[1]).read())
		bf.run()
	except IndexError:
		print("use # anywhere in the code to see the state of the bf array and the position of the pointer (debug)\npress enter with nothing to run")
		bf = BF()
		while (True):
			i = raw_input("& ")
			if (i):
				bf.add(i)
			else:
				bf.run()
				bf = BF()

