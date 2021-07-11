# Uses python3
# @author: Junzhong Loo
# Date: 13/6/2021

import sys

def get_change(m):
    """
    Find minimum number of coins needed to change the 
    input value into coins with denominations 1, 5, 10
    """
    coin_denomination = [1, 5, 10]

    # largest to smallest
    coin_denomination.reverse()

    min_coins_needed = 0

    for coin_value in coin_denomination:
        number_of_coins = m // coin_value
        m -= number_of_coins * coin_value
        min_coins_needed += number_of_coins

    return min_coins_needed

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
