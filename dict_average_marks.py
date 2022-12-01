person={}
cont = True
u_input = "yes"
while True:
    name = input("Enter Student name:")
    marks = int(input("How much did {0} in maths:  ".format(name)))
    print("{0} scored {1} in Maths".format(name,marks))
    u_input = input("Do you want to add another student's score? (Yes/No) :")
    cont = True
    person[name] = marks
    print(person)
    if u_input.lower() == "yes":
       continue
    else:
        break
average = sum(person.values()) / len(person.values())
print(average)