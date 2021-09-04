# python3
# Author: Junzhong Loo
# Date: 3/9/2021

# class Deque():
#     def __init__(self):
#         self.__stack = []
#         self.__auxiliary_stack = []

#     def


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

"""
2 - [2] [2]
7 - [2, 7] [2, 7]
3 - [2, 7, 3] [2, 7, 7]
1 - [2, 7, 3, 1] [2, 7, 7, 7]
5 - [2, 7, 3, 1 ,5] [ 7, 7, 7, 5]
2 - [2, 7, 3, 1, 5, 2] [7, 7, 7, 5,]
"""
