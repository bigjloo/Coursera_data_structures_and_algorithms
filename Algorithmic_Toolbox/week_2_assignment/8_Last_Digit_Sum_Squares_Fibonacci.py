# Last Digit of Sum of Squares of Fibonacci
# @author: Junzhong Loo
# Date: 6/6/2021

def main():
   
    def last_digit_of_sum_squares_fibonacci(n):
        """
        F(1^2)+F(2^2)+...F(n^2) == F(n)*F(n+1)
        """
        pisano_period = 60

        n %= pisano_period

        previous = 0
        current = 1
        for _ in range(n):
            previous, current = current, previous + current

        return (previous * current) % 10
    
    print(last_digit_of_sum_squares_fibonacci(7))

if __name__ == "__main__":
    main()
