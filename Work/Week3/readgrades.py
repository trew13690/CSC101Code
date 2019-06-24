#ReadGrades.py
# Reads a grade file and outputs fot the user

def main():
    
    #Print the reason of the program 
    print('This program will accept a file and output the results ')
    #Ask user for file to read data 
    afileName = input('What is the name of the data file ')
    #Open the file and store the file object
    afile = open('./Week3/'+afileName + '.dat')
    #Read and split the line in the file object
    fileText = afile.read().splitlines()
    #Create a lookup tableA
    grades = ['F','F','F','F','F','D','C','B','A','A']
    #Create a empty list to for new data to be written later
    newdata = []
    #Loop though list data from file object 
    for i in fileText:
        #Remove whitespace    
        studentStats = i.split(' ')
        #Store Human friendly format data
        #Grab the letter grade
        letter_grade = grades[int(studentStats[2])//10-1]
        readable_data = '\nStudent: '+ studentStats[0] +' '+ studentStats[1] +  '\nGrade Points: '+ studentStats[2] + '\nGrade Letter: '+ letter_grade
        #Add new data to write with additional data
        newdata.append(i + ' '+  letter_grade+ '\n')
        #print Human friendly data
        print(readable_data)
    #Write new file by creating file object
    writeFile = open('grades.dat','w')
    #Write lines from new data to new file object
    writeFile.writelines(newdata)
    #Cleanup by closing file object 
    writeFile.close()
    #Cleanup by closing other file object
    afile.close()

#Run program 
main()
