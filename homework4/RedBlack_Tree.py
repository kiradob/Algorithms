class Color:
    BLACK = 0
    RED = 1


class Node:
    def __init__(self, value, color=Color.RED, left=None, right=None):
        # Конструктор класса Node, инициализирует узел дерева.
        self.value = value
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        return f'value={self.value} color={self.color} left={self.left} right={self.right}'


class RedBlackTree:
    def __init__(self, root=None):
        # Конструктор класса RedBlackTree, инициализирует красно-черное дерево.
        self.root = root

    def add_node(self, value):
        # Метод для добавления нового узла в дерево.
        if self.root:
            # Если дерево уже содержит корень
            result = self._add_node(self.root, value)
            self.root = self._rebalance(self.root)
            self.root.color = Color.BLACK
            return result
        else:
            # Если дерево пустое, создаем корень
            self.root = Node(value, Color.BLACK)
            return True

    def _add_node(self, node, value):
        # Рекурсивный вспомогательный метод для добавления узла в дерево.
        if node.value == value:
            return False
        elif node.value > value:
            if node.left:
                is_added = self._add_node(node.left, value)
                node.left = self._rebalance(node.left)
                return is_added
            else:
                node.left = Node(value)
                return True
        else:
            if node.right:
                is_added = self._add_node(node.right, value)
                node.right = self._rebalance(node.right)
                return is_added
            else:
                node.right = Node(value)
                return True

    def _rebalance(self, node):
        # Рекурсивный метод для балансировки дерева после добавления узла.
        result = node
        need_balance = True
        while need_balance:
            need_balance = False
            if (
                result.right and result.right.color == Color.RED and
                (result.left is None or result.left.color == Color.BLACK)
            ):
                # Если правый потомок красный, а левый потомок чёрный или отсутствует
                need_balance = True
                result = self._right_turn(result)
            if (
                result.left and result.left.color == Color.RED and
                result.left.left and result.left.left.color == Color.RED
            ):
                # Если левый потомок красный, и его левый потомок также красный
                need_balance = True
                result = self._left_turn(result)
            if (
                result.left and result.left.color == Color.RED and
                result.right and result.right.color == Color.RED
            ):
                # Если оба потомка красные
                need_balance = True
                self._color_exchange(result)
        return result

    @staticmethod
    def _right_turn(node):
        # Вспомогательный метод для правого поворота вокруг узла.
        right = node.right
        between = right.left
        right.left = node
        node.right = between
        right.color = node.color
        node.color = Color.RED
        return right

    @staticmethod
    def _left_turn(node):
        # Вспомогательный метод для левого поворота вокруг узла.
        left = node.left
        between = left.right
        left.right = node
        node.left = between
        left.color = node.color
        node.color = Color.RED
        return left

    @staticmethod
    def _color_exchange(node):
        # Вспомогательный метод для обмена цветов узлов.
        node.right.color = Color.BLACK
        node.left.color = Color.BLACK
        node.color = Color.RED

    def print_tree(self):
        if self.root:
            self._print_tree(self.root, 'root', 0)
        else:
            print('Пустое дерево.')

    def _print_tree(self, node, node_type, starting_indent):
        # Рекурсивный вспомогательный метод для печати дерева.
        color = '-Black' if node.color == Color.BLACK else '-Red'
        if node_type == 'root':
            print('root--', end='')
            print(f'{node.value}{color}')
            starting_indent += 3
        for i in range(starting_indent // 3 - 1):
            if i == 0:
                print('   ', end='')
            print('|  ', end='')
        if node_type == 'left':
            print(f'L--{node.value}{color}')
        if node_type == 'right':
            print(f'R--{node.value}{color}')
        if node.left or node.right:
            starting_indent += 3
            if node.left:
                self._print_tree(node.left, 'left', starting_indent)
            if node.right:
                self._print_tree(node.right, 'right', starting_indent)
        else:
            starting_indent -= 3