def add(x,y,z):
    return x+y+z
def subtract(x,y,z):
    return x-y-z
def multiply(x,y,z):
    return x*y*z
def divide(x,y,z):
    if y!=0:
        return x/y/z
    else:
        return "Error: Division by zero"
def calculator():
    print("Welcome to the python calculator")
    print("Select operation:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    choice=input("Enter choice(1/2/3/4):")
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    num3=int(input("Enter third number:"))
    if choice=='1':
        print("Result:",add(num1,num2,num3))
    elif choice=='2':
        print("Result:",substract(num1,num2,num3))
    elif choice=='3':
        print("Result:",multiply(num1,num2,num3))
    elif choice=='4':
        print("Result:",divide(num1,num2,num3))
    else:
        print("Invalid input")
