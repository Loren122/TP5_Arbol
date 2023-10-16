from cola import Cola
import linecache


def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split


class NodeTree():

    def __init__(self, value, other_values=None, descripcion=None, capturada=None):
        self.value = value
        self.other_values = other_values
        self.descripcion = descripcion
        self.capturada = capturada
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height >
                           right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):
        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)

            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()

                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)
        __inorden_file(self.root, file_name)

    def _by_lighsaber_color(self, lightsaber_color):
        def __search_by_lightsaber_color(root, lightsaber_color):
            if root is not None:
                __search_by_lightsaber_color(root.left, lightsaber_color)
                value = get_value_from_file('jedis.txt', root.other_values)
                if lightsaber_color in value[4]:
                    print(root.value, value[4].split('/'))
                __search_by_lightsaber_color(root.right, lightsaber_color)
        __search_by_lightsaber_color(self.root, lightsaber_color)

    def jedis_masters_in_file(self):
        def __jedis_masters_in_file(root):
            if root is not None:
                __jedis_masters_in_file(root.left)
                pos = root.other_values
                value = get_value_from_file('jedis.txt', pos)
                if value[3] != '-':
                    print(value[0], value[3])
                __jedis_masters_in_file(root.right)
        __jedis_masters_in_file(self.root)

    def togruta_o_cerean(self):
        def __togruta_o_cerean(root):
            if root is not None:
                __togruta_o_cerean(root.left)
                pos = root.other_values
                value = get_value_from_file('jedis.txt', pos)
                if 'togruta' in value or 'cerean' in value:
                    print(value)
                __togruta_o_cerean(root.right)
        __togruta_o_cerean(self.root)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)
        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena, index):
        def __inorden_start_with(root, cadena, index):
            if root is not None:
                __inorden_start_with(root.left, cadena, index)
                if root.other_values == index and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena, index)
        __inorden_start_with(self.root, cadena, index)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)
        __inorden_start_with_jedi(self.root, cadena)

    def search_by_name(self, name):
        def __search_by_name(root, name):
            if root is not None:
                __search_by_name(root.left, name)
                if root.value == name:
                    pos = root.other_values
                    # print(f'value:(el name) {root.value} - other_values: (el index) {pos}')
                    print(get_value_from_file('jedis.txt', pos))
                __search_by_name(root.right, name)
        __search_by_name(self.root, name)

    def search_by_ranking(self, ranking):
        def __search_by_ranking(root, ranking):
            if root is not None:
                __search_by_ranking(root.left, ranking)
                if root.value == ranking:
                    pos = root.other_values
                    # print(f'value:(el ranking) {root.value} - other_values: (el index) {pos}')
                    print(get_value_from_file('jedis.txt', pos)[0])
                __search_by_ranking(root.right, ranking)
        __search_by_ranking(self.root, ranking)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)
        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)
        __search_by_coincidence(self.root, value)

    def starts_with_and_contains(self, starts_value, contains_value):
        def __search_by_coincidence(root, starts_value, contains_value):
            if root is not None:
                if root.value.startswith(starts_value) or contains_value in root.value:
                    print(root.value)
                __search_by_coincidence(
                    root.left, starts_value, contains_value)
                __search_by_coincidence(
                    root.right, starts_value, contains_value)

        __search_by_coincidence(self.root, starts_value, contains_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count
        return __contar(self.root, value)

    def contar_heroes(self, is_hero):
        def __contar_heroes(root, is_hero):
            count = 0
            if root is not None:
                if root.other_values is is_hero:
                    count = 1
                count += __contar_heroes(root.left, is_hero)
                count += __contar_heroes(root.right, is_hero)
            return count
        return __contar_heroes(self.root, is_hero)

    def contar_nodos(self):
        def __contar_nodos(root):
            count = 0
            if root is not None:
                count = 1
                count += __contar_nodos(root.left)
                count += __contar_nodos(root.right)
            return count
        return __contar_nodos(self.root)

    def dividir_personajes(self, tree_heroes, tree_villanos):
        def __dividir_personajes(root, tree_heroes, tree_villanos):
            if root is not None:
                __dividir_personajes(root.left, tree_heroes, tree_villanos)
                if root.other_values is True:
                    tree_heroes.insert_node(root.value, root.other_values)
                if root.other_values is False:
                    tree_villanos.insert_node(root.value, root.other_values)
                __dividir_personajes(root.right, tree_heroes, tree_villanos)

        __dividir_personajes(self.root, tree_heroes, tree_villanos)

    def insert_node_criaturas(self, value, other_values=None, descripcion=None, capturada=None):
        def __insertar_node_criaturas(root, value, other_values, descripcion, capturada):
            if root is None:
                return NodeTree(value, other_values, descripcion, capturada)
            elif value < root.value:
                root.left = __insertar_node_criaturas(
                    root.left, value, other_values, descripcion, capturada)
            else:
                root.right = __insertar_node_criaturas(
                    root.right, value, other_values, descripcion, capturada)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar_node_criaturas(
            self.root, value, other_values, descripcion, capturada)

    def inorden_criaturas(self):
        def __inorden_criaturas(root):
            if root is not None:
                __inorden_criaturas(root.left)
                print(
                    f'{root.value} - Derrotada por: {root.other_values} - Descripcion: {root.descripcion} - Capturada por: {root.capturada}.')
                __inorden_criaturas(root.right)
        __inorden_criaturas(self.root)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values is not None:
                    if root.other_values not in ranking:
                        ranking[root.other_values] = 1
                    else:
                        ranking[root.other_values] += 1
                __inorden_ranking(root.right, ranking)
        __inorden_ranking(self.root, ranking)

    def criaturas_derrotadas_por(self, vencedor):
        def __inorden_ranking(root, vencedor):
            if root is not None:
                __inorden_ranking(root.left, vencedor)
                if root.other_values == vencedor:
                    if vencedor is not None:
                        print(f'{root.value} fue derrotado por {vencedor}.')
                    else:
                        print(f'{root.value} no fue derrotado por nadie.')
                __inorden_ranking(root.right, vencedor)
        __inorden_ranking(self.root, vencedor)

    def by_level_criaturas(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)

            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(
                    f'{node.value} - Derrotada por: {node.other_values} - Descripcion: {node.descripcion} - Capturada por: {node.capturada}.')

                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def criaturas_capturadas_por(self, cazador):
        def __criaturas_capturadas_por(root, cazador):
            if root is not None:
                __criaturas_capturadas_por(root.left, cazador)
                if root.capturada == cazador:
                    if cazador is not None:
                        print(f'{root.value} fue capturado por {cazador}.')
                    else:
                        print(f'{root.value} no fue capturado por nadie.')
                __criaturas_capturadas_por(root.right, cazador)
        __criaturas_capturadas_por(self.root, cazador)
