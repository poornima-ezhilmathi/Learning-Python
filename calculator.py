def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def quotient(x, y):
    return x % y

def reminder(x, y):
    return x % y

def exponent(x, y):
    return x // y

def square(x, y):
    return x ** y

x=int(input("Enter the first number:"))
y=int(input("Enter the second number"))
choice= input("Enter your choice 1,2,3,4,5,6,7,8")

if x>0 and y>0 and choice in ('1','2','3','4','5','6','7','8'):
    if choice == '1':
        print(add(x,y))
    elif choice == '2':
        print(subtract(x, y))
    elif choice == '3':
        print(multiply(x,y))
    elif choice == '4':
        print(divide(x, y))
    elif choice == '5':
        print(quotient(x, y))
    elif choice == '6':
         print(reminder(x, y))
    elif choice == '7':
          print(exponent(x, y))
    elif choice == '8':
         print(square(x, y))
    next_operation = input("Do you wish to continue? (yes/no):")
    if next_operation == "no":
       exit()
else:
    print("Invalid input")