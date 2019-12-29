# tipo de datos listas

'append', 'clear', 'copy', 'count',
'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort'

variable_lista_new = [1, 22, 0]
variable_lista = [1, 'hola', 2]
variable_lista2 = [12, 'nissan']
variable_lista_vacia = list()

print(variable_lista)

variable_lista.append(121)
variable_lista.append(1212)

print(variable_lista)

# variable_lista.remove('hola')
print(variable_lista)

a = variable_lista.count('hola')
print(a)

variable_copia = variable_lista.copy()

print(variable_copia.remove(2))

# print(variable_copia)
# print(variable_lista)
# variable_lista.clear()
# print(dir(variable_lista))

variable_lista.extend(variable_lista2)
# print(variable_lista)

c = variable_lista2.index(12)
# print(c)

variable_lista2.insert(0, 'paul')

# print(variable_lista2)
variable_lista2.pop(0)

# print(variable_lista2)

variable_lista2.reverse()

# print(variable_lista2)

# variable_lista_new.sort()
# print(variable_lista_new)

