#loops.py will compute the feul efficiency of a multi-leg journey

def main():
    print('Welcome to the efficient fuel program!\n')
    data = []
    data = promptUser()
    print("This is the data for each leg")
    for num in range(len(data)):
        print('_' * 20)
        print("Leg "+ str(num) + '| MPG was at :' + str(data[num])+ ' miles')
        print("_" * 20)

    print("Have a great day! :D") 

def calculateMPG(initalOdometer, lastOdometer, gasUsed):
    """
    calculateMPG will take a inital odometer reading and a last reading and gas used

    Args:
        initalOdometer(float): Reading of the odometer before leg
        lastOdometer(float): Reading of the odometer at end of leg
        gasUsed (float): Usage of gas during the leg in gallons

    Returns:
        mpg (float): The rate of miles per gallon 
    """

    _initalOdometer = initalOdometer
    _lastOdometer = lastOdometer
    _gasUsed = gasUsed

    deltadistance = _lastOdometer - _initalOdometer
    mpg = deltadistance/ gasUsed
    return mpg

def promptUser():
    """
        Ask the user for data to calculate mpg;
    
    Args:
        None
    Returns:
        None
    """
    legs = []
    
    while True:
        print("Please print done when done entering in data")
        initialOdometer = input("Please enter reading of the odometer for the new leg: ")
        lastOdometer = input("Please enter the the reading of the odmeter at the end of the leg: ")
        gasUsed = input("How much gas was used? (in gallons) :  ")
        if initialOdometer =='done' or lastOdometer == 'done' or gasUsed == 'done':
            return legs
        legs.append(calculateMPG(float(initialOdometer),float(lastOdometer), float(gasUsed)))
        
main()