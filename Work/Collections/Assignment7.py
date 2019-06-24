#Sieve of Eratosthenes program

def main():
    # Hold all composite numbers
    
    
    #Ask user for input
    upperBound = input("Enter the number you wish to find primes in: ")
    upperBound = int(upperBound)
    #Set 0 and 1 as primes 
    isCompositeNumbers = [None] * (upperBound+1)
    isCompositeNumbers[0] = 1
    isCompositeNumbers[1] = 1
    #Compute the primes 
    Sieve(int(upperBound), isCompositeNumbers)


def Sieve(upperBound,compositeNumber):
    """
        computes the primes of given upperBound

        Params:
            upperBound: List 
            compositeNumber: List

        Returns:
            None
    """
    # 2 - number you wish to find primes
    # unmarked is prime
    # First one that is marked all compoiites are not prime
    # To create a more effienct process square the next prime and jump to that number to declare as not prime ex 3^2 is 9 
    # if the squared is bigger than number of primes 

    #find primes up to N
    # For all numbers a: from 2 to sqrt(n)
    #  if a is unmarked then 
    #      a is prime
    #      for all multiples of a  (a<n)
    #       mark multiples as compostie
    # all unmarked numbers are prime!



    i = 2 # start the while loop at number 2 
    primes = []
    while i*i <= upperBound:
        print('\nSelecting number '+ str(i)+ '\n')
        if i*i <= upperBound:
            for a in range(i*i,upperBound, i):
                compositeNumber[a] = 1
                print(str(a) + ' is added as a composite of ' + str(i))
        i = i + 1 
    for a in range(len(compositeNumber)):
        if compositeNumber[a] != 1:
            primes.append(a)
            print("Adding prime number "+ str(a) )
    
    print("The composites are " + str(compositeNumber))
    results = "The prime numbers for " + str(upperBound) + " is " + str(primes)
    print(results);



main()