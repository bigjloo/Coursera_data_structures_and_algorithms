# Uses python3
# Author: Junzhong Loo
# Date: 4/9/2021
import sys
import random

# credits to geeksforgeeks.com

def partition3(a, l, r):
    """ Uses 4 pointers with the last element as pivot element """
    # set last element as pivot
    pivot = a[r]

    # left
    i = l 
    j = r - 1
    # right
    p = l 
    q = r - 1

    while i < j:
        # move i to where everything to the left of a[i] is less than pivot
        while a[i] < pivot:
            i += 1
        
        # move j to where everything to the right of a[j] is greater than pivot
        while a[j] > pivot:
            j -= 1
            # edge case where everything to left is greater than pivot
            if (j == l):
                break
        
        # a[i] is now greater or equal to pivot, a[j] is now less or equal to pivot
        # swap a[i] with a[j]
        a[i], a[j] = a[j], a[i]
        
        # a[i] is now less or equal to pivot, a[j] is now greater or equal to pivot
        # check if equal to pivot. if it is, move to the end
        if (a[i] == pivot):
            p += 1
            a[i], a[p] = a[p], a[i]

        if (a[j] == pivot):
            q -= 1
            a[j], a[q] = a[q], a[j]
        
        # now a[i] is less than pivot, a[j] is greater than pivot, loop continues
    
    # i >= j. On the left side of a[i] is less than pivot with the equals at the end. same for other side
    # example:
    # [4,4,4,1,2,3,2,1,5,6,8,6,4,4,4,4] // where 4 is pivot

    # get pivot equal to middle
    # m = end of left partition
    # k = start of left partition
    m = i - 1
    k = l
    # p = right adjacent index to where equal to pivot ends
    while k < p:
        a[k], a[m] = a[m], a[k]
        k += 1
        m -= 1

    # k = start of right partition
    # n = end of right partition
    k = r - 1 
    n = i + 1
    while k > q:
        a[k], a[n] = a[n], a[k]
        k -= 1
        n += 1

    return (p, q)

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    # original m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1- 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
