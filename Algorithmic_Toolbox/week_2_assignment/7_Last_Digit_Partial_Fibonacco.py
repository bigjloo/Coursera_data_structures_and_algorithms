# Last Digit of Sum of Partial Fibonacci
# @author: Junzhong Loo
# Date: 6/6/2021

def main():
    def calculate_pisano_period(m):
        """ 
        find mod m where start with 0,1 
        For any value of 'm', the Pisano Period is greater than m and strictly less than m*m
        """

        # Pisano period always start with 01
        previous = 0
        current = 1

        for i in range(0, m*m):
            previous, current = current, (previous + current) % m

            # found a period start with 01
            if (previous == 0 and current == 1):
                return i + 1
    
    def last_digit_of_sum_of_partial_fibonacci(a, b):
        """ 
        start sum from point a
        """
        # last digit == mod 10 == pisano_period of 60
        pisano_period = calculate_pisano_period(10)
        
        b %= pisano_period

        # find previous and current from point a
        previous = 0
        current = 1
        for _ in range(a - 1):
            previous, current = current, previous + current
        
        sum = current
        for _ in range(b - a):
            previous, current = current, previous + current
            sum += current
        
        return sum % 10

    print(last_digit_of_sum_of_partial_fibonacci(10, 200))

if __name__ == "__main__":
    main()
