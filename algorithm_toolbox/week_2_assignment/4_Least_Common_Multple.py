# Least Common Multiple
# @author: Junzhong Loo
# Date: 6/6/2021
import math 


def main():
    def efficient_GCD(a, b):
        """ 
        Using Euclids algorithn where GCD(a,b) == GCD(b, a%b). 
        Break down problem into smaller problem
        """
        if b == 0:
            return a
        
        return efficient_GCD(b, a % b)
    
    def least_common_multiple(a, b)-> int:
        """
        LCM(a,b) == (a * b)/ GCD(a,b)
        """
        return (a * b)/efficient_GCD(a, b)

    print(least_common_multiple(761457, 614573))

if __name__ == "__main__":
    main()