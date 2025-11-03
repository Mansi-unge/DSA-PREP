# counting bits program 

# taking input 
n = int(input("enter any number to count bits in it :"))

n_binary = bin(n)[2:]
print("binary form of n is :",n_binary)

print("bits in n_binary is :",n_binary.count('1'))