import sleep

# def puntos_por_caja(caja):
#     puntos = ''
#     if caja == 'sorpresa':
#         puntos = '10 puntos'
#     elif caja == 'caja verde':
#         puntos = '5 puntos'
#     else:
#         puntos = '0 puntos'
#     return puntos
#     print('esta linea')
#
#
# a = puntos_por_caja('sorpresa')
# b = puntos_por_caja('caja verde')
# c = puntos_por_caja('caja roja')
# print(a, b, c)


# def iterar_elementos(**args):
#     for i in args.items():
#         print(i)
#
# iterar_elementos(a='mario', b='pedro')


def suma(a=10, b=20, c=10):
    return a + b + c

s = suma(a=100)
print(s)
