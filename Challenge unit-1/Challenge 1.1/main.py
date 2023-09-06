#Implementing a recursive function to calculate the factorial of a given number.

def fact_recursive(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_recursive(n-1)

number=int(input("Enter a value : "))
result=fact_recursive(number)

print("\nThe factorial of {} : {}".format(number,result))
