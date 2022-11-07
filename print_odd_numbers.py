def odd_number():
    print("Enter a number:")
    val = int(input())
    print("You entered : '<{0}>'".format(val))
    print("How many odd numbers you wish to print?:")
    pnum = int(input())
    out = 0
    print("Printing {0} odd numbers after {1}:".format(pnum, val))
    for i in range(out,pnum):
        if val %2 == 0:
            val = val + 1
        else:
            val = val + 2
        print(val)
odd_number()

