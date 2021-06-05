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

    user_input = int(input("Enter fib number: "))
    answer = naive_fib_last_digit(user_input)
    print(answer)

if __name__ == "__main__":
    main()