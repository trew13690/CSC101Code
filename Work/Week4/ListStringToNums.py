# ConvertStringToNumbers

def main():

    print('Welcome to the string to number program')
    resultList = input('please enter some numbers: ')
    resultList = resultList.split(',')
  
    toNumbers(resultList)
    print('Your result was ' + str(resultList))
    print('The type in the list is as follows: ')

    printTypeofList(resultList)

#Print Type of what is in the list
def printTypeofList(resultList):
    for i in range(len(resultList)):
        print(str(type(resultList[i])) + ' '+ str(resultList[i]))

#Convert StringList to Numbers 
def toNumbers(strList):
    for i in range(len(strList)):
        resultList[i] = float(strList[i])
        
main()
