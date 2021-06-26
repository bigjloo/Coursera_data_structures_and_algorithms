# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    """
    check if trip is possible by comparing the distance of 
    the two furthest stops from each other with full tank m

    while d > 0:
        find furthest stop we can go on full tank
        distance -= stop distance from start
        slice stops list
        count += 1
    """
    # Find max distance between stops
    # If tank is less than the max distance,
    # goal is not reachable. Return -1
    stops_copy = stops[:]
    stops_copy.append(distance)
    stops_sorted = sorted(stops_copy)
    max_between_stops = stops_sorted[-1] - stops_sorted[-2]
    if tank < max_between_stops:
        return -1
    
    # CONTINUE
    last_stop = 0
    stops = 0
    while distance > 0:
        for i in range(len(stops)):
            if tank < stops[i]:
                last_stop += i-1
                stops += 1
                distance -= stops[i-1]
                tank += stops[i-1]
                stops = stops[i:]
                break

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
