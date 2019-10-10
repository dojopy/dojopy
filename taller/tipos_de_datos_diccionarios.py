#TIPO DE DATOS DICCIONARIOS
variable_dict = {'pedro': 'aprende python', 'henry': 'ensena python'}

variable_dict_vacia = {}
print(variable_dict)
print(variable_dict_vacia)

print(variable_dict['pedro'])
print(variable_dict.get('pedro', 'no existe'))
print(variable_dict.keys())
print(variable_dict.values())
print(variable_dict.items())

variable_dict['nueva_clave'] = 'clave genial'
variable_dict.pop('pedro')

variable_dict.update({'otra clave': 'otro valor'})
print(variable_dict)


# print(variable_dict.keys())
# print(variable_dict.values())


# variable_dict['nueva_clave'] = 'bien'
# print(variable_dict)
# print(dir(variable_dict))
# print(variable_dict.keys()+ variable_dict.values())
# print(list(variable_dict.iteritems()))
