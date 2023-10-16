from arbol_binario import BinaryTree

# 6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento,
# color de sable de luz, ranking(Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:


file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()


# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie

name_tree = BinaryTree()
ranking_tree = BinaryTree()
specie_tree = BinaryTree()

read_lines.pop(0)

for index, linea_jedi in enumerate(read_lines):

    jedi = linea_jedi.split(';')
    jedi.pop()
    name_tree.insert_node(jedi[0], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
    specie_tree.insert_node(jedi[2], index+2)

# b. realizar un barrido inorden del árbol por nombre y ranking

name_tree.inorden()
print()
ranking_tree.inorden()
print()


# c. realizar un barrido por nivel de los árboles por ranking y especie

ranking_tree.by_level()
print()
specie_tree.by_level()
print()


# d. mostrar toda la información de Yoda y Luke Skywalker

name_tree.search_by_name('yoda')
name_tree.search_by_name('luke skywalker')
print()


# e. mostrar todos los Jedi con ranking “Jedi Master”

ranking_tree.search_by_ranking('jedi master')
print()

# f. listar todos los Jedi que utilizaron sable de luz color verde

name_tree.search_by_lighsaber_color('green')
print()

# g. listar todos los Jedi cuyos maestros están en el archivo

name_tree.jedis_masters_in_file()
print()


# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”

specie_tree.togruta_o_cerean()
print()


# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

name_tree.starts_with_and_contains('a', '-')
