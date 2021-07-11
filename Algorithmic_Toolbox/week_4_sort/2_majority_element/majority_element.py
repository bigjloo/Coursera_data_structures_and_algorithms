# Uses python3
import sys

def get_majority_element(a, left, right):
    """ Boyer Moore agorithm - O(n) """
    candidate = None
    count = 0
    for num in a:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    if count < 1:
        return -1
        
    majority = len(a)/2
    second_count = 0
    for num in a:
        if candidate == num:
            second_count += 1

    return 1 if second_count > majority else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
