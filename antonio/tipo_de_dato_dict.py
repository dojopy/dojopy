
variable_dict = {'key':'valor', 'key1': 'valo'}
variable_dict_vacio = dict()

print(variable_dict)
print(variable_dict_vacio)


print(variable_dict['key'])
print(variable_dict.get('key0101', 'vacio'))

print(dir(variable_dict))
print(variable_dict.pop('key'))
#print(variable_dict)

variable_dict.update({'antony': 'nice'})

variable_dict['mascota'] = 'gato'


print(variable_dict.keys())
print(variable_dict.values())