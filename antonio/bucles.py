import time

# Bucles For y While

#Bucles For #
lista_de_tareas = ['programar', 'leer', 'ejercicios']

print(len('hola'))

otra_lista = range(7) #genera una lista con 7 numeros consec.

for x in lista_de_tareas:
	#print(x.replace('programar', 'codear'))
	if x == 'leer':
		print('leer sobre negocios')

	for y in otra_lista:
		if len(x) == y:
			print('mi elemento', x, 'tiene', y, 'caractes')


#---------------------
#Bucle While
#lista_nueva = range(100)

variable = 50000

while variable:
	time.sleep(5)
	print('numero', variable)
	variable = variable - 1
	if variable == 5:
		break

# crear un temporzador que luego de un tiempo determiando
# imprima un mensaje



