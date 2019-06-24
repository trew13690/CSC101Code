#Slope Program 

def main():

    #Tell user what the program is :D 
    print('Welcome to the Slope Program! \nPlease follow directions! \n')
    
    #Ask user for two points
    point_1_x = float(input('Enter x for first point? '))
    print(str(point_1_x))
    print('First point is ' + '[' + str(point_1_x) + ', ] so far \n')

    point_1_y= float(input('Enter y for first point: '))
    print(str(point_1_y))
    print('First point is '+ '['+ str(point_1_x) + ', ' + str(point_1_y) + '] \n')

    point_2_x = float(input('Enter x for second point? '))
    print(str(point_1_x))
    print('Second point is ' + '[' + str(point_2_x) + ', ] so far \n')

    point_2_y = float(input('Enter y for second point? '))
    print(str(point_2_y))
    print('Second point is '+ '['+ str(point_2_x) + ', ' + str(point_2_y) + ']\n')


    #Do calculation

    slope =  (point_2_y-point_1_y)/(point_2_x-point_1_x)
    print('The slope is '+ str(slope))

    #Return Results

if __name__ == '__main__':
    main()