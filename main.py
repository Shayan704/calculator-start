#Add
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multification
def multiply(n1,n2):
  return n1*n2

#Division
def division(n1,n2):
  return n1/n2

from art import logo
print(logo)

symbols={"+":add,
      "-":subtract,
      "*":multiply,
      "/":division}

def calculator():
  num1=float(input("Enter the first number?: "))
  
  for sign in symbols:
    print(sign)
  
  condition='y'
  while(condition=='y'):
    operation= input("Pick the operation from the above line: ")
    num2=float(input("Enter the next number?: "))
    
    calculation_function= symbols[operation]
    result=calculation_function(num1, num2)
    
    print(f"{num1} {operation} {num2} = {result}")
    condition=input("Type y to continue and Type n to exit. ").lower()
    if(condition=='y'):
      num1=result  
    else:
      calculator()

calculator()
      
    

