class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, nodes=[]):
        self.node = None
        self.height = -1
        self.balance = 0

        for node in nodes:
            self.insert(node)

    def height(self):
        return self.node.height if self.node else 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.node
        newnode = Node(key)

        if tree is None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key <= tree.key:
            self.node.left.insert(key)
        else:
            self.node.right.insert(key)

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node is None:
            self.balance = 0
        else:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height

    def delete(self, key):
        if self.node is not None:
            if self.node.key == key:
                if (self.node.left.node is None) and (self.node.right.node is
                                                      None):
                    self.node = None
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement is not None:
                        self.node.key = replacement.key
                        self.node.right.delete(replacement.key)
            elif key < self.node.key:
                self.node.left.delete(key)
            else:
                self.node.right.delete(key)

            self.rebalance()

    def logical_predecessor(self, node):
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                node = node.right.node
        return node

    def logical_successor(self, node):
        node = node.right.node
        if node is not None:
            while node.left is not None:
                if node.left.node is None:
                    return node
                node = node.left.node
        return node

    def inorder_traverse(self):
        if self.node is None:
            return []

        inlist = []
        left_nodes = self.node.left.inorder_traverse()
        for i in left_nodes:
            inlist.append(i)

        inlist.append(self.node.key)

        left_nodes = self.node.right.inorder_traverse()
        for i in left_nodes:
            inlist.append(i)

        return inlist
