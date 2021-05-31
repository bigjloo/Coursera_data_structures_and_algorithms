# MaximumPairwiseProduct
# @author: Junzhong Loo
# Date: 30/5/2021

def main():
    """
    Implement program that works in less than one second even on huge datasets.
    MaximumPairwiseProduct finds the largest multiplication of two numbers in a given array
    """
    import math
    import time
    import random

    def maxPairwiseProduct(numbers: list)-> int:
        """
        iterates through a list and finds the largest multiply of two elements O(n^2)
        """
        length = len(numbers)
        if length == 0:
            return 
       
        if length == 1:
            return numbers[0]

        max = -math.inf
        for i in range(length):
            if i == length - 1:
                break
            for j in range(i + 1, length):
                if numbers[i]*numbers[j] > max:
                    max = numbers[i] * numbers[j]
        return max
    
    def fastMaxPairwiseProduct(numbers: list) -> int:
        """
        more efficient algo which just takes the largest two numbers and multiple O(2n)
        """
        largest_number = max(numbers)
        numbers.remove(largest_number)
        second_largest_number = max(numbers)
        return largest_number * second_largest_number


    
    def generateRandomNumbersList(numbers_count: int)-> list:
        lst = []
        for i in range(numbers_count):
            lst.append(random.randint(1,10000))
        return lst

    # test_numbers = [2, 9,5,6,7,7,8,8,4,9,9,9,9,9,9,9,9,9,9,9,9,9]
    numbers = generateRandomNumbersList(10000)
    #print("Test numbers:", test_numbers)
    #print("Test numbers:", numbers)
    start_time = time.time()
    print("Result:",maxPairwiseProduct(numbers))
    end_time = time.time()
    print("Time taken: ", end_time - start_time)
    start_time = time.time()
    print("Result:",fastMaxPairwiseProduct(numbers))
    end_time = time.time()
    print("Time taken: ", end_time - start_time)

if __name__ == "__main__":
    main()