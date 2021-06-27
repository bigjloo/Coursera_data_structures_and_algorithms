# python3
import sys


def compute_min_refills(distance, tank, stops):

    n = len(stops)
    # Add goal to stops
    stops.append(distance)
    # Add initial starting point to stops
    stops = [0] + stops
    # Initialize refill count and current index position in stops list
    refill_count = 0
    current_position = 0
    # run while current position is not destination. destination = n + 1
    while current_position <= n:
        # Set our new starting point
        last_position = current_position
        # keep moving up one station until the next station refill not possible ie find max stops before refill
        while current_position <= n and (stops[current_position + 1] - stops[last_position] <= tank):
            current_position += 1
        # If no stops for refill that satisfy tank max distance requirements
        # return -1
        if current_position == last_position:
            return -1
        # After finding best stop for refill and not at destination
        # refill +1
        if current_position <= n:
            refill_count += 1

    return refill_count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
