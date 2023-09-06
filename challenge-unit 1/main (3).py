def fact(n):
  if(n==0):
    return 1
  else:
    return(n*fact(n-1))
n=int(input("Enter the value of n:"))
print("The Factorial of",n,'is',fact(n))