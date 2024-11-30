#Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter a number: "))
print(f"Fibonacci number at position {n} is {fibonacci(n)}")
