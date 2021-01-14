class Tree:
    """ Abstract base class representing a tree structure """
    class Position:
        """ Abstract representation of position of an element """
        def element(self):
            """ Return the element stored at these position """
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            """ Returns True if this position is same as the other """
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """ Returns True if this position is not same as the other """
            raise NotImplementedError('Must be implemented by subclass')

    def root(self):
        """ Return position representing the root (None if empty) """
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, p):
        """ Returns True if p is root element """
        return self.root() == p

    def is_leaf(self, p):
        """ Returns True if p has no child """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Returns True if the Tree is empty """
        return len(self) == 0

    def parent(self, p):
        """ Returns the Position represent of p's parent  """
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        """ Returns the number of children p has """
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        """ Returns the iteration of Position representing p's child """
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        """ Returns the total number of elements in the Tree """
        raise NotImplementedError('Must be implemented by subclass')

    def __iter__(self):
        """ Generate an iteration of the elements of the tree """
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """ Generates the iterations of positions """
        return self._preorder()

    def _preorder(self):
        """ Pre order traversal of the tree """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """ Generates the iterations of positions """
        return self._preorder()

    def _postorder(self):
        """ Post order traversal of the tree """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
        yield p

