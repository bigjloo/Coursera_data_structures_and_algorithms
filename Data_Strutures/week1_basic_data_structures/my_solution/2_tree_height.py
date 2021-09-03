#  Author: Junzhong Loo
# python3
import sys
import threading
from queue import Queue


def compute_height(n, parents):
    tree = {}
    root = parents.index(-1)
    for i in range(n):
        try:
            tree[parents[i]].append(i)
        except KeyError:
            tree[parents[i]] = [i]
    q = Queue()
    q.put(root)
    level = 0
    while not q.empty():
        level += 1
        node_left_in_q = q.qsize()
        while node_left_in_q > 0:
            node_left_in_q -= 1
            current_node = q.get_nowait()
            try:
                children = tree[current_node]
                for child_node in children:
                    q.put(child_node)
            except KeyError:
                continue

    return level


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    # n = 100
    # parents = list(map(int, "50 73 65 90 58 60 80 94 -1 38 15 23 42 73 56 8 61 9 30 86 45 30 57 8 45 66 69 80 22 66 53 2 48 22 86 30 44 8 60 98 82 24 91 21 8 65 77 77 62 54 26 47 46 75 29 15 67 23 54 81 28 86 66 18 72 60 8 18 92 48 9 15 76 8 81 57 48 76 7 71 28 23 29 30 57 76 29 89 66 2 30 7 44 27 37 29 57 6 66 36".split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# sys.modules[__name__] = compute_height

# def test():
