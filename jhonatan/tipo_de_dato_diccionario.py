
# tipo de dato dict

variable_dict = dict()
print(variable_dict)

variable_dict_new = {'key': 'value', 'key2': 'valu2'}

variable_dict_2 = {'autos': 'tesla'}

print(dir(variable_dict_new))

# z = variable_dict_new['key28']
d = variable_dict_new.get('key289', 'vacio')
# print(d)

f = variable_dict_new.keys()
print(f)

t = variable_dict_new.values()
print(t)

# variable_dict_new.clear()
print(variable_dict_new)

# variable_dict_2.pop('key2')

print(variable_dict_new)

variable_dict_2.update(variable_dict_new)
print(variable_dict_2)


g = variable_dict_new.items()
print(g)
