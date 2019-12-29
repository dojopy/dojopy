
# tipo ded dato string

variable_string = ''
variable_string_vacio = str()
variable_autos = 'FerrarI ferra rI vochido'
variable_conteo = '100'

#print(variable_string)
#print(variable_string_vacio)
#print(variable_autos)


new_var =  variable_autos.replace('ferra' , 'marca')
#print(new_var)

# #print(dir(new_var))

convert_mayus = variable_autos.upper()
#print(convert_mayus)

convert_minus = variable_autos.lower()
#print(convert_minus)

convet_tile = variable_autos.capitalize()
#print(convet_tile)

search_init = variable_autos.startswith('ferra')
#print(search_init)

search_init = variable_autos.endswith('ferra')
#print(search_init)

es_numero = variable_conteo.isdigit()
#print(es_numero)

var_search = variable_autos.find('barni')
# print(var_search)

var_split = variable_autos.split('rI')
# print(var_split)