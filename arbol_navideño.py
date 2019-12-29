from random import choice
from time import sleep

adornos = ['^', 'o']
number_rows = 25

while True:
	sleep(0.3)
	print('\033[93m'+'\t\t\t\t Merry Christmas by Dojopy!')
	for x in range(0,number_rows):
		a = ' '*(number_rows-x) + '*'*x
		b = '*'*x
		a = list(a)
		a.insert(choice([number_rows,number_rows-x]), choice(adornos))
		a = ''.join(a)

		b = list(b)
		b.insert(choice([0, x+1]), choice(adornos))
		b = ''.join(b)
		print('\033[92m'+'{}{}'.format(a,b))
	print('\n')