# User select a number between 1-100
user_number= int(input("Please enter a nubmer between 1-100: "))

# determine if the number is even or odd 
if user_number %2 == 0:
    print(f"The number {user_number} is even" )
else: 
    print(f"The number {user_number} is odd" )
