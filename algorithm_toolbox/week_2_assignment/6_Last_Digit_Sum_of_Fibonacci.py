# Last Digit of the Sum of Fibonacci Numbers
# @author: Junzhong Loo
# Date: 6/6/2021    

def main():
    """
    find last digit of sum of F(n)
    """
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

    def sum_of_last_digit_fibonacci(n):
        """
        last digit == mod 10
        """   
        pisano_period = calculate_pisano_period(10) # pisano_period == 60

        n %= 60

        # sum all last digit 
        previous = 0
        current = 1
        sum = 0
        for _ in range(n - 1):
            previous, current = current, previous + current
            sum += current
        return (sum + 1) % 10

    print(sum_of_last_digit_fibonacci(3))

if __name__ == "__main__":
    main()