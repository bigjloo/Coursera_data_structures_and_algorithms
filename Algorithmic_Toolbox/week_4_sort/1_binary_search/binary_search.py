# Uses python3
import sys

def binary_search(a, x):
    def b_search(a, left_index, right_index, element):
        """ Binary search algo"""
        # Target not in array
        if right_index < left_index:
            return -1

        mid_index = (left_index + right_index) // 2
        if a[mid_index] == element:
            return mid_index
        elif a[mid_index] > element:
            return b_search(a, left_index, mid_index - 1, element)
        else:
            return b_search(a, mid_index + 1, right_index, element)

    left, right = 0, len(a)-1
    output = []
    for element in x:
        output.append(b_search(a, left, right, element))
    return output

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
    
