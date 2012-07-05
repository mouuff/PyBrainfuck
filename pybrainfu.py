from sys import stdout

__all__ = ('BF')

def BF(script):
	''''Launch a Brainfuck script'''
	table = [0]*3000
	pointer = 0
	progress = 0
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
					stdout.write(chr(table[pointer]))
				except ValueError:
					stdout.write("?")
				stdout.flush()
				
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
	return set(table)

if __name__ == '__main__':
	print BF("""
++++++++++
[
	>+++++++>++++++++++>+++>+<<<<-
] Loop init
>++.
>+.
+++++++.
.
+++.
>++.
<<+++++++++++++++.
>.
+++.
------.
--------.
>+.
>.
""")
