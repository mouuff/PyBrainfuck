from sys import stdout, argv

__all__ = ('BF')

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
						if (loop <= 0):
							progress = 0
							script = script[script.find("]")+1:]
		progress += 1
	print list(set(table))
	return out

if __name__ == '__main__':
	try:
		print BF(open(argv[1]).read())
	except (IOError, IndexError):
		print("Error, file not found or arguements error")
		
