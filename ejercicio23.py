from arbol_binario import BinaryTree

# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

criaturas = [
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tifón', 'derrotado': 'Zeus'},
    {'name': 'Equidna', 'derrotado': 'Argos Panoptes'},
    {'name': 'Dino', 'derrotado': None},
    {'name': 'Pefredo', 'derrotado': None},
    {'name': 'Enio', 'derrotado': None},
    {'name': 'Escila', 'derrotado': None},
    {'name': 'Caribdis', 'derrotado': None},
    {'name': 'Euríale', 'derrotado': None},
    {'name': 'Esteno', 'derrotado': None},
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Ladón', 'derrotado': 'Heracles'},
    {'name': 'Águila del Cáucaso', 'derrotado': None},
    {'name': 'Quimera', 'derrotado': 'Belerofonte'},
    {'name': 'Hidra de Lerna', 'derrotado': 'Heracles'},
    {'name': 'León de Nemea', 'derrotado': 'Heracles'},
    {'name': 'Esfinge', 'derrotado': 'Edipo'},
    {'name': 'Dragón de la Cólquida', 'derrotado': None},
    {'name': 'Cerbero', 'derrotado': None},
    {'name': 'Cerda de Cromión', 'derrotado': 'Teseo'},
    {'name': 'Ortro', 'derrotado': 'Heracles'},
    {'name': 'Toro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Jabalí de Calidón', 'derrotado': 'Atalanta'},
    {'name': 'Carcinos', 'derrotado': None},
    {'name': 'Gerión', 'derrotado': 'Heracles'},
    {'name': 'Cloto', 'derrotado': None},
    {'name': 'Láquesis', 'derrotado': None},
    {'name': 'Átropos', 'derrotado': None},
    {'name': 'Minotauro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Harpías', 'derrotado': None},
    {'name': 'Argos Panoptes', 'derrotado': 'Hermes'},
    {'name': 'Aves del Estínfalo', 'derrotado': None},
    {'name': 'Talos', 'derrotado': 'Medea'},
    {'name': 'Sirenas', 'derrotado': None},
    {'name': 'Pitón', 'derrotado': 'Apolo'},
    {'name': 'Cierva de Cerinea', 'derrotado': None},
    {'name': 'Basilisco', 'derrotado': None},
    {'name': 'Jabalí de Erimanto', 'derrotado': None},
]

criaturas_tree = BinaryTree()

for criatura in criaturas:
    criaturas_tree.insert_node_criaturas(
        criatura['name'], criatura['derrotado'])

# a. listado inorden de las criaturas y quienes la derrotaron
print('a. inorden:')
criaturas_tree.inorden_criaturas()
print()


# b. se debe permitir cargar una breve descripción sobre cada criatura

def agregar_descripcion(tree, name, descripcion):
    value = tree.search(name)

    if value:
        value.descripcion = descripcion


# c. mostrar toda la información de la criatura Talos

def mostrar_informacion(tree, name):
    value = tree.search(name)

    if value:
        print(
            f'{name} - Derrotada por: {value.other_values} - Descripcion: {value.descripcion} - Capturada por: {value.capturada}.')


agregar_descripcion(criaturas_tree, 'Talos',
                    "Protegía a la Creta minoica de piratas e invasores")

print('c.')
mostrar_informacion(criaturas_tree, 'Talos')
print()

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas

dic_ranking = {}

criaturas_tree.inorden_ranking(dic_ranking)


def order_por(item):
    # print(item)
    return item[1]


ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print('d.')
print(ordenados[:3])
print()

# e. listar las criaturas derrotadas por Heracles

print('e.')
criaturas_tree.criaturas_derrotadas_por('Heracles')
print()


# f. listar las criaturas que no han sido derrotadas

print('f.')
criaturas_tree.criaturas_derrotadas_por(None)
print()


# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo

def capturada_por(tree, nombre, capturada):
    value = tree.search(nombre)

    if value:
        value.capturada = capturada


capturada_por(criaturas_tree, 'Quimera', 'Piratas')


# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó

capturada_por(criaturas_tree, 'Cerbero', 'Heracles')
capturada_por(criaturas_tree, 'Toro de Creta', 'Heracles')
capturada_por(criaturas_tree, 'Cierva de Cerinea', 'Heracles')
capturada_por(criaturas_tree, 'Jabalí de Erimanto', 'Heracles')


# i. se debe permitir búsquedas por coincidencia

print('i. Coincidencia "A"')
criaturas_tree.search_by_coincidence('A')
print()


# j. eliminar al Basilisco y a las Sirenas

criaturas_tree.delete_node('Sirenas')
criaturas_tree.delete_node('Basilisco')


# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derrotó a varias

def cambiar_vencedor(tree, name, vencedor_nuevo):
    value = tree.search(name)

    if value:
        value.other_values = vencedor_nuevo


cambiar_vencedor(criaturas_tree, 'Aves del Estínfalo', 'Heracles')
agregar_descripcion(
    criaturas_tree, 'Aves del Estínfalo', 'Heracles derrotó a varias de ellas')


# l. modifique el nombre de la criatura Ladón por Dragón Ladón

def cambiar_nombre(tree, name, new_name):
    value = tree.search(name)
    if value:
        value.value = new_name


cambiar_nombre(criaturas_tree, 'Ladón', 'Dragón Ladón')


# m. realizar un listado por nivel del árbol

print('m. by_level:')
criaturas_tree.by_level_criaturas()
print()


# n. muestre las criaturas capturadas por Heracles.

print('n.')
criaturas_tree.criaturas_capturadas_por('Heracles')
