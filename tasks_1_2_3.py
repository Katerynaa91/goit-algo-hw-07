"""Завдання 1. Напишіть алгоритм (функцію), який знаходить 
найбільше значення у двійковому дереві пошуку або в AVL-дереві.

Завдання 2.
Напишіть алгоритм (функцію), який знаходить 
найменше значення у двійковому дереві пошуку або в AVL-дереві.

Завдання 3.
Напишіть алгоритм (функцію), який знаходить 
суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
"""

class Node:
    def __init__(self, node) -> None:
        self.node = node
        self.left = None
        self.right = None
    def insert(self, data):
        if self.node is None:
            self.node = Node(data)
        else:
            if data < self.node:
                if not self.left:
                    self.left = Node(data)
                self.left.insert(data)
            elif data > self.node:
                if not self.right:
                    self.right = Node(data)
                self.right.insert(data)

    def findMin(self):
        """Метод, який знаходить найменше значення у двійковому дереві пошуку"""
        if not self.node:
            return "Tree is empty"
        minn = self
        while minn.left:
            minn = minn.left
            return minn.left.node
    
    def findMax(self):
        """Метод, який знаходить найменше значення у двійковому дереві пошуку"""
        if self.node is None:
            return 0
        maxx = self

        while maxx.right:
            if maxx.right.node > maxx.node:
                maxx = maxx.right
        
        return maxx.node

    def show(self):
        if self.left:
            self.left.show()
        if self.node:
           print(self.node)
        if self.right:
            self.right.show()


def summ(root):
    """Функція для розрахунку суми значень всіх вузлів бінарного дерева"""
    if root is None:
        return 0
    return (root.node + summ(root.left) + summ(root.right))


# nodes = [1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18, 20, 25, 2, 25]

tree = Node(10)
tree.insert(5)
tree.insert(16)
tree.insert(2)
tree.insert(7)
tree.insert(13)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(9)
tree.insert(11)
tree.insert(15)
tree.insert(18)
tree.insert(25)

# tree.show()
print(tree.findMin())
print(tree.findMax())
print(summ(tree))

