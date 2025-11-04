
def is_prime(n):
  if n <= 1:
    print("invalid number or it is not prime..")
  else:
    for i in range (2,n):
      if n % i == 0:
        print("it is not a prime number...")
        return
  print("it's a prime number....")


n = int(input("enter any number to find is it prime or not :"))
print("number you entred is :",n)
is_prime(n)
