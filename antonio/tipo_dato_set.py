
variable_set = {'item', 'item2', 'item3', 'item'}
variable_set_vacio = set()
print(variable_set)
print(variable_set_vacio)
print(dir(variable_set))

variable_set.remove('item')
print(variable_set)

variable_set.pop()

variable_set.update({'hola'})

variable_set.add('tiger')
print(variable_set)
