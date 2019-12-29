
# tipo de dato lista

# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse',
# 'sort'


variable_lista = [12, 'auto', True, 'auto']

variable_lista_animales = ['perro', 'gato', 'loro']

variable_lista_num = [12,21, 2, 1]

lista_vacia = list()  # tambien []

print(variable_lista)
print(lista_vacia)

# print(dir(variable_lista))

variable_lista.append('moto')

element = variable_lista[-1]
contar = len(variable_lista)
new_contar = variable_lista[len(variable_lista) - 1]
# print(element)
# print(new_contar)
# print(contar)

# print(variable_lista.index('moto'))

# variable_lista.clear()
# print(variable_lista)

# print(variable_lista.count('auto'))

# variable_lista.remove(12)
# print(variable_lista)

# variable_lista.reverse()
# print(variable_lista)

# variable_lista.pop(1)
# print(variable_lista)

#variable_lista_animales.sort()
# print(variable_lista_animales)

#variable_lista_num.sort()
# print(variable_lista_num)


# variable_lista_animales.extend(variable_lista_num)
# print(variable_lista_animales)

print(variable_lista_animales)
ultimo = len(variable_lista_animales)
print(ultimo)

variable_lista_animales.insert(0, 'conejo')
print(variable_lista_animales)