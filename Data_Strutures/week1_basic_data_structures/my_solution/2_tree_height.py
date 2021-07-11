# python3

import queue
import sys
import threading
from queue import Queue

class Node:
    def __init__(self, parent=None):
            self.parent = parent
            self.children = []

    def __str__(self):
        return "parent: {}, children: {}".format(self.parent, self.children)

    def add_child(self, node):
        self.children.append(node)
    
    def number_of_children(self):
        return len(self.children)
        

def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height
    nodes = []
    for _ in range(n):
        nodes.append(Node())
    for i in range(n):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].add_child(nodes[i])
    
    # traverse down tree until no more children
    # +1 for height every step down
    # n -= len(children)
    # if children = 0 and n == 0: return height
    # elif children != 0
    # traverse again
    
    # edge case: no children for root

    # height = 0
    # def traverse(node, height, n):
    #     # no children. all nodes explored
    #     if len(node.children) == 0:
    #         pass
    #     if n == 0:
    #         return height
    #     # theres children
    #     height += 1
    #     n -= node.number_of_children()
    #     for node in node.children:
    #         traverse(node, height, n)
    
    # height = traverse(root, height, n - 1)
    # return height

    queue = Queue()
    unexplored_node = n
    def get_height(node, height):
        queue.put(node)
        




def main():
    # n = int(input())
    # parents = list(map(int, input().split()))
    n = 5
    parents = list(map(int, "4 -1 4 1 1".split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
