from arbol_binario import BinaryTree

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe(MCU),
# desarrollar un algoritmo que contemple lo siguiente:


# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo
# booleano que indica si es un héroe o un villano, True y False respectivamente

lista_marvel = [
    {'nombre': 'iron man', 'heroe': True},
    {'nombre': 'thanos', 'heroe': False},
    {'nombre': 'capitan america', 'heroe': True},
    {'nombre': 'red skull', 'heroe': False},
    {'nombre': 'hulk', 'heroe': True},
    {'nombre': 'black widow', 'heroe': True},
    {'nombre': 'rocket raccon', 'heroe': True},
    {'nombre': 'dotor strage', 'heroe': True},
    {'nombre': 'doctor octopus', 'heroe': True},
    {'nombre': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

for personaje in lista_marvel:
    arbol.insert_node(personaje['nombre'], personaje['heroe'])

arbol.inorden()
print()


# b. listar los villanos ordenados alfabéticamente

def villanos_alfabetico(tree):
    tree.inorden_super_or_villano(False)


villanos_alfabetico(arbol)
print()


# c. mostrar todos los superhéroes que empiezan con C

def super_c(tree):
    tree.inorden_start_with("C", True)


super_c(arbol)
print()


# d. determinar cuántos superhéroes hay el árbol

def cont_super(tree):
    print(tree.contar_heroes(True))


cont_super(arbol)
print()


# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre

def cambiar_nombre(tree, nombre_a_cambiar, nombre_nuevo):
    pos = tree.search(nombre_a_cambiar)

    if pos:
        is_hero = pos.other_values
        tree.delete_node(nombre_a_cambiar)
        tree.insert_node(nombre_nuevo, is_hero)


cambiar_nombre(arbol, "dotor strage", "doctor strange")
arbol.inorden()
print()


# f. listar los superhéroes ordenados de manera descendente

def super_ordenados(tree):
    tree.inorden_super_or_villano(True)


super_ordenados(arbol)
print()


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:

arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

arbol.dividir_personajes(arbol_heroes, arbol_villanos)

arbol_heroes.inorden()
print()
arbol_villanos.inorden()
print()


# I. determinar cuántos nodos tiene cada árbol

print(arbol_heroes.contar_nodos())
print()
print(arbol_villanos.contar_nodos())
print()


# II. realizar un barrido ordenado alfabéticamente de cada árbol.

arbol_heroes.inorden()
print()
arbol_villanos.inorden()
