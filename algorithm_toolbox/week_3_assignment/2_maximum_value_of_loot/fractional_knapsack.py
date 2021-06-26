# Uses python3
#from _typeshed import WriteableBuffer
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    """
    while not full:
        choose i with best value/weight ratio
        if item < capacity, take all
        else
            take as much as possible
        return total value and amounts taken
    """
    # calculate value/weight for all
    vw = {}
    # vw = { i: value/weight, ...}
    for i in range(len(weights)):
        vw[i] = values[i] / weights[i]

    while capacity > 0:
        # get item w highest vw ratio
        max_key = max(vw, key=lambda key: vw[key])
        if weights[max_key] <= capacity:
            value += values[max_key]
            capacity -= weights[max_key]
            vw.pop(max_key)
        else:
            value += capacity / weights[max_key] * values[max_key]
            return round(value, 4)

    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
