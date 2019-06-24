


def Level(Ncredits):
    classlevel = "None"

    if Ncredits<45: classlevel = "Freshman"
    
    elif Ncredits >=45 and Ncredits <= 89 : classlevel = "Sophomore"
    elif Ncredits >= 90 and Ncredits <=135: classlevel = "Junior"
    else:  classlevel = "Senior"
    #Write the rest of the code needed to classify each student

    print("Student is a",classlevel)

Level(42)
Level(45)
Level(90)
Level(135)
Level(136)
