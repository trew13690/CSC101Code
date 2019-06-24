#A5Script.py

def main():

    #Take the user entered credits
    Ncredits =  input("Please enter the number of credits earned: ")
    #Ensure input is corret format
    correct_formatCredits = CheckInput_Convert(Ncredits)
    #Determine grade Level
    gradeLevel  = lookupGradeLevel(correct_formatCredits)
    #Print results
    print("\nYou are a",gradeLevel)

def CheckInput_Convert(input)->float:
    """
        Handles any exceptions in input as well as make into the correct format

        Parameters:
            input (str): the input of the user

        Returns:
            correctFormat (float)
    """
    formatedInput = 0
    try:
        formatedInput = float(input)
        return formatedInput
    except ValueError as error :
        print('You entered in the wrong type of input, only except numbers\nPlease try again\n')
        exit()
    else:
        print('You did something that I do not even know 0.0')
        exit()


    
def lookupGradeLevel(credits)-> str:
    """
        Looks up your grade level depending on the credit you have taken

        Parameters:
            credits (float): Take the credits that the user is taking
        
        Returns:
            GradeLevel (str): The grade level the user belongs to
    """
    GradeLevel = None
    if(credits >= 0 and credits <= 6 ):
        GradeLevel = 'Freshman'
        return GradeLevel
    elif(credits >= 7 and credits <= 15 ):
        GradeLevel = 'Sophomore'
        return GradeLevel
    elif(credits >= 16 and credits <= 25 ):
        GradeLevel = 'Junior'
        return GradeLevel
    elif(credits >= 26 ):
        GradeLevel = 'Senior'
        return GradeLevel
    else:
        return 'Error....'        

main()