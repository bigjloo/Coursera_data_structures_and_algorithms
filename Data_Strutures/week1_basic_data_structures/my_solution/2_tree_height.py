# python3
import sys
import threading
from queue import Queue


# class Node:
#     def __init__(self, parent=None):
#         self.parent = parent
#         self.children = []

#     def __str__(self):
#         return "parent: {}, children: {}".format(self.parent, self.children)

#     def add_child(self, node):
#         self.children.append(node)

#     def number_of_children(self):
#         return len(self.children)

#     def add_parent(self, parent):
#         self.parent = parent

#     def __repr__(self):
#         return f"Node(parent: {self.parent}, children: {self.children}"


def compute_height(n, parents):
    tree = {}
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            continue
        try:
            tree[parents[i]].append(i)
        except KeyError:
            tree[parents[i]] = [i]
    print(root)
    print(tree)
    q = Queue()
    q.put(root)
    level = 0
    # while not q.empty():
    #     vertex = q.get_nowait()
    #     try:
    #         children = tree[vertex]
    #         level += 1
    #         for child_node in children:
    #             q.put(child_node)
    #     except KeyError:
    #         continue

    def bfs(tree, level):
        if tree == None:
            return level
        level += 1
        max_level = max(bfs(node, level) for node in tree)
        return max_level

    return bfs(tree, level)


def main():
    # n = int(input())
    # parents = list(map(int, input().split()))
    n = 100
    parents = list(map(int, "96 61 95 34 12 26 48 42 69 74 90 67 8 53 65 0 14 47 88 8 49 4 93 75 6 29 -1 62 87 12 42 52 1 46 4 83 14 75 72 95 15 86 29 53 85 78 65 31 5 96 6 74 87 24 15 90 22 85 20 46 78 97 50 97 69 19 21 61 92 5 22 47 63 1 93 28 20 34 52 21 72 88 67 0 86 49 63 48 28 25 50 83 31 19 62 24 64 64 92 25".split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
