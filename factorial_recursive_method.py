
def factorial(n):
  if n == 0 or n == 1:
    return 1 
  return n * factorial(n-1)

n = int(input("enter any number : "))
print("number you entred is :",n)
print("factorial of number n is :",factorial(n))