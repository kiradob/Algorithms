# создание нодов, создание бинарного дерева, добавление значения, удаление значения, подсчет количества элементов.
class Node:
    def init(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        res = f'значение нашего узла: {self.value}'
        # if self.left and self.right:
        # res = f'значение нашего узла: {self.value}, значения левого: {self.left.value}, значение правого: {self.right.value}' 
        if self.left:
            res +=  f' значение левого: {self.left.value}'
        if self.right:
            res +=  f' значение правого: {self.right.value}'            
        return res
class Tree:
    def init(self, root = None):
        self.root = root

def search(self, node, data, parent = None):

    if node is None:
        return None, parent, False 
    if data == node.value:
        return node, parent, True

    if data > node.value: 
        if node.right:
            self.search(node.right, data, node)
    if data < node.value:
        if node.left:
            self.search(node.left, data, node)
    return node, parent, False

def add_node(self, value):
    res = self.search(self.root, value)
    if not res[2]:
        new_node = Node(value)
        if value > res[0].value:
            res[0].right = new_node
        else:
            res[0].left = new_node
    else:
        print('Ой все, такое значение уже есть')

# def print_tree(self):
initial_node = Node(15)

tree_1 = Tree(initial_node)

print(initial_node)
tree_1.add_node(16)
print(initial_node.right)
print(initial_node)
print(tree_1.search(initial_node, 16))