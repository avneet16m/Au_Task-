# Two number sum program in Python

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate sum
total = num1 + num2

# Display result
print("The sum is:", total)
#####
def fib (n):
    if n==0 or  n==1:
        return  1
    else:
        return fib (n-1)+fib(n-2)
    ###
    def star(n):
        for  i in range (1,n):
            print(i"*")