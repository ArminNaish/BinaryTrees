from __future__ import annotations
from queue import Queue
from dataclasses import dataclass
from typing import Union, Optional

# https://www.cs.princeton.edu/courses/archive/fall02/cos126/exercises/trees.html

@dataclass()
class Node:
    value: Union[int, str]
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __lt__(self, other):
        return self.value < other.value

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_balanced(self):
        if self.left is None or self.right is None:
            return False
        return abs(self.left.count(preorder) - self.right.count(preorder)) <= 1

    def from_preorder(values):
        tree = Node(values[0])
        for value in values[1:]:
            tree.add(Node(value))
        return tree

    def sequence(self, traverse):
        sequence = []
        for node in traverse(self):
            sequence.append(node.value)
        return sequence

    def add(self, node):
        if node < self:
            if self.left:
                self.left.add(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.add(node)
            else:
                self.right = node

    def count(self, traverse):
        count = 0
        for _ in traverse(self):
            count += 1
        return count

    def sum(self, traverse):
        sum = 0
        for node in traverse(self):
            sum += node.value
        return sum

    def max(self, traverse):
        max = 0
        for node in traverse(self):
            if node.value > max:
                max = node.value
        return max

    def nodes_less_than(self, value, traverse):
        for node in traverse(self):
            if node.value < value:
                yield node 

    def nodes_greater_than(self, value, traverse):
        for node in traverse(self):
            if node.value > value:
                yield node

    def depth(self):
        max_level = 1
        def traverse(node, level=1):
            nonlocal max_level
            if level > max_level: 
                max_level = level
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
        traverse(self)
        return max_level

    def max_cost(self):
        max_cost = 0
        def traverse(node, cost=0):
            nonlocal max_cost
            cost += node.value
            if cost > max_cost: 
                max_cost = cost
            if node.left:
                traverse(node.left, cost)
            if node.right:
                traverse(node.right, cost)
        traverse(self)
        return max_cost


def preorder(node):
    stack = []
    stack.append(node)
    while len(stack) > 0:
        current = stack.pop()
        yield current
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def levelorder(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        current = queue.get()
        yield current
        if current.left:
            queue.put(current.left)
        if current.right:
            queue.put(current.right)

def inorder(node):
    if node.left:
        yield from inorder(node.left)
    yield node
    if node.right:
        yield from inorder(node.right)

def postorder(node):
    if node.left:
        yield from postorder(node.left)
    if node.right:
        yield from postorder(node.right)
    yield node

def pretty_print(node, indent=0):
    print(f'{" "*indent}{node.value}')
    if node.left:
        pretty_print(node.left,indent+2)
    if node.right:
        pretty_print(node.right, indent+2)

