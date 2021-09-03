# python3
# Author: Junzhong Loo
# Date: 3/9/2021
# Use an auxiliary stack for O(1) retrieval for Max function
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__auxiliary_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__auxiliary_stack) == 0:
            self.__auxiliary_stack.append(a)
        else:
            # compare and add to stack
            top_of_auxiliary_stack = self.__auxiliary_stack.pop()
            if a > top_of_auxiliary_stack:
                self.__auxiliary_stack.extend([top_of_auxiliary_stack, a])
            else:
                self.__auxiliary_stack.extend(
                    [top_of_auxiliary_stack, top_of_auxiliary_stack])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__auxiliary_stack.pop()

    def Max(self):
        top_of_auxiliary_stack = self.__auxiliary_stack.pop()
        self.__auxiliary_stack.append(top_of_auxiliary_stack)
        return top_of_auxiliary_stack


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
