# Converstion Program ~ 


#Main Function
def main(*args,**kwargs):
   
    Num = input('Please enter a US dollar amount to convert: ')
    us_amount = float(Num)
    us_to_can_dollar_conversion(us_amount)

# #Conversion fuction ~ takes a number and print converted num to Celsius
# def convert(num):
#     celsius = (num -32 )* 5/9 
#     print(str(celsius))


#Converstion Function ~ takes a US dollar to a Can doller
def us_to_can_dollar_conversion(us_amount):
    cand_amount = us_amount * 1.33
    print('US dollars $' + str(us_amount))
    print('Candian dollars $'+ str(cand_amount))

if __name__ == '__main__':
    main()

