#Stats.py Compute the Mean and Median out of a Odd number of numbers in ordered list

def main():
    
    #Starts Stat Program Instruction 
    print('\nWelcome to the Stat Program\nBEWARE, ENTER ONLY SEQUENCES AMOUNTING LEN[...] == ODD ')
    print('PLEASE ONLY ENTER LIST OF NUMBERS SEPARTED BY ,  AND MUST BE IN ORDER \n')
    #Print and store a list of numbers to be computed
    n = ((input('Please enter your list of numbers to be computed? : ')).split(','))

    #Grab the length of the list
    nLength = len(n)

    #Setup storage for sum and median 
    sum = 0
    median = 0

    #loop though first half of sequence adding to sum 
    for i in range(int(nLength/2)):
        sum = sum + int(n[i])
        print('Counting your wishs @: '+ str(sum))

    #Next number is the median
    print('\nComputing median...and drawing breath')  
    median = n[int(nLength/2)]

    #Add median to the sum 
    sum = sum + int(median)
    print('the half way is here...wherever that is ..\n  ')

    #Loop though the second half of sequence adding to sum 
    for i in range (int(nLength/2)):
        sum = sum + int(n[(int(nLength/2)+1)+i])
        print('Counting your disappointments @: '+ str(sum))
    
    #Store the mean
    mean = float(sum/nLength)

    #Print the result to the user
    print('\nGiven a moment to consider your question....\nI have come to the conclusion\n')
    print('The stats for this sequence of numbers is :\nMedian: '+ str(median)+ '\nMean: '+ str(mean))

main()





