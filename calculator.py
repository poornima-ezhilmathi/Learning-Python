# Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def divide(x, y):
    return x % y

def divide(x, y):
    return x // y


print("Choose an option from the following")
print("(1) Add(+)")
print("(2) Subtract(-)")
print("(3) Multiply(*)")
print("(4) Divide(/)")
print("(5) Find Remainder(%)")
print("(6) Find Quotient(//)")
print("(7) Find Square of a number(**)")


while True:
    # input from the user
    choice = input("Enter your choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6','7'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))

        elif choice == '5':
            print(x, "%", y, "=", divide(x, y))

        elif choice == '6':
            print(x, "//", y, "=", divide(x, y))

        elif choice == '7':
            print(x, "**", y, "=", divide(x, y))

        next_operation = input("Let's do next calculation? (yes/no): ")
        if next_operation == "no":
            break

    else:
        print("Not a valid option")