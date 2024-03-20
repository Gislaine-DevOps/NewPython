# Writing the translation usinf functions
# number= int(input("enter a number: "))

def even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
    
result = even_odd(25)
print(result)
result = even_odd(62)
print(result)
