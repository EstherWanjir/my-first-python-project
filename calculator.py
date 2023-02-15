#This is a calculator project
x=eval(input("enter  a number:"))
y=eval(input("enter another number:"))

operator= input("enter operator:")
 
def add (num1,num2):
    result=num1+num2
    print (result)

def subtract(num1,num2):
    result=num1-num2
    print(result)

def divide(num1,num2):
    result=num1/num2
    print(result)

def multiply(num1,num2):
    result=num1*num2
    print (result)

if operator == "+":
    add(x,y)
elif operator =="-":
    subtract(x,y)
elif operator == "/":
    divide(x,y)
elif operator =="X" or "operator"=="x" or "operator"=="*"  :
    multiply(x,y) 
else:
    print("invalid error")

             
