
# tipo de dato String

variable_string = str()
var_hola = 'HolA mundo que tal'
var_numeero = 10
var_str = '100'
new_var = str(var_numeero)
# print(new_var)
# print(type(new_var))
# new_conv = int(var_str)
# print(new_conv)
# print(type(new_conv))


# metodos que aplican a un tipo de dato String
var_hola = var_hola.replace('jdieiweiji', 'auto')
# print(var_hola)
 
var_mayus = var_hola.upper()
# print(var_hola)

var_minus = var_hola.lower()
# print(var_minus)

# print(dir(var_minus))

var_capit = var_hola.capitalize()
# print(var_capit)

var_cont = var_hola.count('dedede')
# print(var_cont)

var_1 = var_hola.isdigit()
var_2  = var_str.isdigit()
# print(var_1)
# print(var_2)

var_find = var_hola.find('barni')
# print(var_find)

var_split = var_hola.split('que')
# print(var_split)

var_start = var_hola.startswith('mundo')
# print(var_start)

var_end = var_hola.endswith('tal')
print(var_end)
