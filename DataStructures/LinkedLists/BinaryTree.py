from Tree import Tree


class BinaryTree(Tree):
    """ Abstract representation of Binary Tree """

    def left(self, p):
        """ Returns Position representing left of p """
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        """ Returns Position representing right of p """
        raise NotImplementedError('Must be implemented by subclass')

    def sibling(self, p):
        """ Returns Position of p's sibling """
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """ Generates iteration of Positions representing p's children """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """ Generates the sequence of positions """
        return self._inorder()

    def _inorder(self):
        """ Travers a binary tree in inorder """
        for p in self._subtree_inorder(self.root()):
            yield p

    def _subtree_inorder(self, p):
        """ Generates inorder iteration of positions in subtree """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
