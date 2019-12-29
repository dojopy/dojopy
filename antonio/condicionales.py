
# condiciones
lista_de_tareas = ['jugar', 'estudiar']
variable = 15
otra_var = ''

if variable >= 15:
	print('genial es verdadera')
else:
	print('es falsa :s')

if 'data' in lista_de_tareas:
	print('genial vamos a jugar')
else:
	print('a estudiar :s')


if variable and lista_de_tareas and otra_var:
	print('todas son verdaderas :D')
else:
	print('es falsa :s')


# condiciones anidadas
if variable != 15:
	print('genial es verdadera')
elif variable < 30:
	print('mayor a 30')
else:
	print('otro codigo')


if variable:
	if lista_de_tareas:
		print('lista tiene elementos')
		if variable > 1:
			print(':D')
	print('hola')