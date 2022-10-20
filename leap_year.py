def leap_year():
    i = int(input("Enter an year"))
    print("Checking if",i, "is a Leap Year")
    if (i%400==0):
       print(i, "is a Leap Year as it's divisible by 400")
    elif (i%100==0):
           print(i, "is not a Leap Year as it's divisible by 100 but not by 400 ")
    elif (i%4==0):
           print(i, "is a Leap Year as it's divisible by 4 but not by 100 or 400")
    else:
        print("Not a leap year")

leap_year()

