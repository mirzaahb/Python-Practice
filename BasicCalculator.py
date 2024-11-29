#Basic Calculator

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

x = float(input("Please enter the first number: "))
y = float(input("Please enter the second number: "))
Answer = 0

print("1. Multiplication \n 2.Division \n 3.Addition \n 4.Subtraction")
n = int(input("Please choose an operation by entering the number of the listing: "))

if n == 1:
    Answer = multiplication(x, y)
    print(Answer)

elif n == 2:
    Answer = division(x, y)
    print(Answer)

elif n == 3:
    Answer = addition(x, y)
    print(Answer)

elif n == 4:
    Answer = subtraction(x, y)
    print(Answer)

else:
    print("Please enter a number within the range")
