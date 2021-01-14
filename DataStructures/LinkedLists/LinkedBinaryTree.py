from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """ Linked representation of binary tree """
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('Element must be of proper Position type')
        if p._container is not self:
            raise ValueError('Element does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('Element is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, el):
        if self._root is not None:
            raise ValueError('Root already exists')
        self._size = 1
        self._root = self._Node(el)
        return self._make_position(self._root)

    def _add_left(self, pr, el):
        node = self._validate(pr)
        if node._left is not None:
            raise ValueError('Left child already exists')
        self._size += 1
        node._left = self._Node(el, node)
        return self._make_position(node._left)

    def _add_right(self, pr, el):
        node = self._validate(pr)
        if node._right is not None:
            raise ValueError('Right chlid already exists')
        self._size += 1
        node._right = self._Node(el, node)
        return self._make_position(node._right)

    def _replace(self, p, el):
        node = self._validate(p)
        old = node._element
        node._element = el
        return old
