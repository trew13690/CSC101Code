# Assignment4.py is a program that shows the understanding of functions, parameters and return values

#Main function is called first
def main():
    #Open data file by the user input
    fileName = input('What is the name of the file: ')
    #Create file object
    datafile = open('./Week4/'+ fileName,'r')
    #Read data and store as list
    listdata = datafile.readlines()
    #Print list data to user
    print(str(listdata) + ' [Data loaded]')
    #Change the str entries in list to int
    toNumbers(listdata)
    #Square each entry in list 
    squareEach(listdata)
    #Get the sum of the squence 
    sum = sumList(listdata)
    #Display the results to the user
    print('The sum of the squence is :' + str(sum))

#Function takes List[int] and squares each entry in list 
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    print(str(nums)+ ' has been squared')

#Function takes List[int] and adds up each entry to get the sum of the sequence
def sumList(nums):
    sum = 0 
    for i in range(len(nums)):
        sum = sum + nums[i]
        print('Sum equals now :' + str(sum))
    return sum 

#Function take List[str] and converts each entr to an int
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])




main()
