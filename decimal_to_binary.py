# write a program to convert decimal to binary 

decimal = int(input("enter any number to convert it from decimal to binary : "))

binary  = bin(decimal)[2:]

print("binary form of decimal number ",decimal,"is",binary)