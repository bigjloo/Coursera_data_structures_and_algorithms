# SumOfTwoDigits.py
# @author: Junzhong Loo
# Date: 30/5/2021

def main():
    """
    Reads two digits from std input and prints their sum 
    """
    user_input = input()
    split_numbers = user_input.split(" ")
    int_split_numbers = map(lambda x: int(x),split_numbers)
    sum = 0
    for number in int_split_numbers:
        sum += number
    print(sum)

if __name__ == "__main__":
    main()