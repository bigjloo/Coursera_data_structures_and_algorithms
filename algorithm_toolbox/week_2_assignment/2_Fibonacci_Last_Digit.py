# Fib last digit   
# @author: Junzhong Loo
# Date: 5/6/2021

def main():
    def naive_fib_last_digit(n):
        """ last digit of fib(n) is exactly the sum of last digit fib(n-1) + fib(n-2) """
        if n <= 1:
            return n

        previous = 0
        current  = 1

        for _ in range(n - 1):
            previous, current = current, previous + current

        return current % 10

    def efficient_fib_last_digit(n):
        """ 
        Read up Pisano Period
        for modulo 10, the last digits repeats itself in cycles of 60
        """
        n = n % 60
        output = naive_fib_last_digit(n-1) + naive_fib_last_digit(n-2)
        return output % 10

    user_input = int(input("Enter fib number: "))
    efficient_answer = efficient_fib_last_digit(user_input)
    print(efficient_answer)


if __name__ == "__main__":
    main()