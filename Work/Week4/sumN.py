

def main():
    num_to_sum = input('Enter numbers to sum: ')
    print('\nThis is the sum of your sequence: '+ str(sumN(num_to_sum))+ '\n')
    print('\nThis is the sum of your sequence cubed: ' + str(sumNCubes(num_to_sum)))

def sumN(n):
    sum = 0
    n = int(n)
    for i in range(n):
        sum = sum + i
        print('Counting your entitlements...@: '+ str(sum)  )
    return sum

def sumNCubes(n):
    sum = 0
    n = int(n)
    for i in range(n):
        sum = sum + i**3
        print('Calculating your terrible bad ideas..@ '+ str(sum))
    return sum


main()
