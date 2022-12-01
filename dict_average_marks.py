person={}
name = input("Enter name")
marks = int(input("Enter marks: "))

cont = True
uinput = "yes"
while True:
    if uinput == "no":
       break
    else:
        cont = True
        person[name] = marks
        print(person)
        average = sum(person.values()) / len(person.values())
        print(average)
        uinput = input("continue ")
        continue
#print(employees)