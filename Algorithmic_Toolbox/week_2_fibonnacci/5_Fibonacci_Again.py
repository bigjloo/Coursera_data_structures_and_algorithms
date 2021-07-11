# Fibonacci Again
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
    
    def fib_again(n, m):
        """ 
        computer Fib(n) mod m
        every mod period starts with 01,
        find the pisano period(p) length -> find n mod p -> calc
        eg: pisano period == 8 for mod 3
        2015 == 251*8 + 7
        F(2015) mod 3 == F(7) mod 3 == 1
        """
        if n <= 1:
            return n

        pisano_period = calculate_pisano_period(m)

        remainder = n % pisano_period

        previous = 0
        current = 1
        for _ in range(remainder - 1):
            previous, current = current, previous + current
        
        return current % m

    print(fib_again(2816213588, 239))

if __name__ == "__main__":
    main()