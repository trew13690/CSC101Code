#username.py
# Simple string processing program to generate usernames.

def main():
    print("This program generates computer usernames. \n ")
    
    # Get the user's first and last names 
    first = input('Please enter your first name: ')
    last = input('Please enter your last name: ')

    # Concat first initial with 7 chars of the last name
    uname = first[0] + last[:7]
    print("Your user name is: ", uname)

main()