# Greatest common divisor
# @author: Junzhong Loo
# Date: 5/6/2021    

def main():
    def efficient_GCD(a, b):
        """ 
        Using Euclids algorithn where GCD(a,b) == GCD(b, a%b). 
        Break down problem into smaller problem
        """
        if b == 0:
            return a
        
        return efficient_GCD(b, a % b)

    print(efficient_GCD(320,24))


if __name__ == "__main__":
    main()
