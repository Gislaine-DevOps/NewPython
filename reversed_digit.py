# write a program that prints digit(s) of a number in reverse order on the same line
# get user input
number = int(input("write your digit(s) here: "))
# Check if the number has only one digit
if number < 10: # knowing that 10 is the first number with 2 digits
    print("Only one digit:", number)
else:
    # Print the digits in reverse order using % 10
    print("Digits in reverse order:", end="")
    while number > 0:
        last_digit = number % 10
        print(last_digit, end="")
       
    

    
