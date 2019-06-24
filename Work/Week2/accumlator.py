#ACCUMULATOR PROGRAM

def main():

    print('Welcome to the Accumulator Program!!! \n')
    n = int(input('Enter # of days you sold books? '))
    acc = 0
    
    for i in range(n):
        acc = acc + int(input("How many books sold on day " + str(i+1)+ ': ')) 
       
    print('You have sold these many books this month: ' + str(acc))


if __name__ == '__main__':
    main()