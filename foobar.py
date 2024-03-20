# Requesting a number from 0-50 from a user
number= int(input("input a number from 0-50: "))

if number >= 50:
    print("Number isn't from 0-50 try again!")
elif ((number %7 == 0)  and (number %5 == 0)): 
    print("FooBar")
elif number %5 == 0:
    print("Foo")
elif number %7 == 0:
    print("Bar")
    


