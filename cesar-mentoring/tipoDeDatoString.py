var_string_vacia = ''

print('mi variablle vacia es:', var_string_vacia)

variable_string = '\t hola cesar MUNDO cesar salto \t'
print(variable_string)

nueva_var = variable_string.replace('cesar', 'henry')
print(nueva_var)

new_var_mayus = variable_string.upper()
print(new_var_mayus)

new_var_minus = variable_string.lower()
print(new_var_minus)

new_var_cont = variable_string.count('auto')
print(new_var_cont)

#new_var_inicial = variable_string.endswith('hola')
#print(new_var_inicial)

new_var_part = variable_string.split('cesar')
print(new_var_part)

new_var_find = variable_string.find('ferrari')
print(new_var_find)

new_title = variable_string.capitalize()
print(new_title)

#print(dir(variable_string))

new_var_clear = variable_string.strip()

print(variable_string)
print(new_var_clear)