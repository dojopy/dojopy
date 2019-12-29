# estas lineas leen un archivo
# texto_genial = open('texto.txt', 'r')
# print(texto_genial.read())

mi_data = 'genial mago'

# nuevo_archivo = open('./otro_archivo.txt', 'a')
# lista = nuevo_archivo.write('\n\tnueva linea ;)')
# nuevo_archivo.close()


with open('otro_archivo.txt', 'a+') as f:
    print(f.readlines())
