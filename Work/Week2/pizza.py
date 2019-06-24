# Numbers Program ~ Compute price per square inch of pizza 
import math
from colorama import init, Fore,Back
from termcolor import colored

def main():
    
    #Explain the program 
    init()
    CalculatePizza()

def CalculatePizza():
    print(colored('Pizza Program :D \nHow much will it cost to fill my stomach per square inch!!!!! ', 'green'))
    #Ask the user for the values: diameter and price
    dia = float(input("What is the diameter of the pizza in inchs: "))
    price = float(input( " What is the price: $"))
    #Calcuate the Radius from the diameter
    cost = CostPerInch(dia, price)
    #Report the Result
    print(colored('The cost of the pizza per square inch is : $' + str(round(cost,3)),'red'))

def CostPerInch(dia, price):
    #Calcuate the Radius from the diameter
    radius = dia/2
    #Calculate the area radius 
    area = math.pi*radius**2
    #Divide to find cost per square inch 
    cost = area/price
    return cost

if __name__ == '__main__':
    main()