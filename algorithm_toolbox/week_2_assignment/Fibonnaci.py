# Fibonacci efficient
# @author: Junzhong Loo
# Date: 5/6/2021    
import time

def main():
    def fibonacci(n):
        """ naive Fibonacci algorithm """
        if n == 0 or n == 1:
            return 1
        
        return fibonacci(n-1) + fibonacci(n-2)

    def fastFibonacci(n, memo={}):
        """ more efficient fibonacci algorithm using memoization """
        if n == 0 or n == 1:
            memo[n] = 1
            return memo[n]
        try:
            return memo[n]
        except KeyError:
            memo[n] = fastFibonacci(n-1) + fastFibonacci(n-2)
            return memo[n]

    # get user input for fibonacci
    n = int(input("Enter a positive integer for Fib: "))

    start_time = time.time()
    answer = fibonacci(n)
    end_time = time.time()
    naive_time_taken = end_time - start_time
    print("naive time: ", naive_time_taken)

    start_time = time.time()
    answer = fastFibonacci(n)
    end_time = time.time()
    fastFib_time_taken = end_time - start_time
    print("efficient time: ", fastFib_time_taken )
    print(f"fib({n}): ", answer)

if __name__ == "__main__":
    main()