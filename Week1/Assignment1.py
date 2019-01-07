
#Main function
def main(*arg, **kwargs):

    # User inputs a value
    value = input('Please enter a value: ')

    # Print value
    print(value)
    
    #Square the value
    sq_value = int(value)**2

    # print the square of the value
    print('The value squared ' + value + ' is ' + str(sq_value))


if __name__ == '__main__':
    main()
