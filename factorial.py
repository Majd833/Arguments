def factorial(x):
    '''This is a recrusive function to find the factorial of the following numbers'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 6 is:",factorial(6))