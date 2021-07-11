# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)

        if next in ")]}":
            # Process closing bracket, write your code here
            if not are_matching(opening_brackets_stack.pop()[0], next):
                return i + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch) if mismatch else print("Success")



if __name__ == "__main__":
    main()
