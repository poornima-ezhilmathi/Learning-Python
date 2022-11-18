def print_fibonacci():
    print("Enter a number:")
    num = int(input())
    print("You entered : '<{0}>'".format(num))
    print("How many fibonacci numbers you wish to print?:")
    pnum = int(input())
    print("Printing {0} fibonacci numbers after {1}:".format(pnum, num))
    count =0
    val =0
    val1 =1
    if num == 1:
        print(val1)
        pnum=pnum-1
    while count < pnum:
           if val1>num:
              print(val1)
           else:
               pnum +=1
           if val >= 0:
               # print(val1)
               out = val + val1
               val = val1
               val1 = out
               #print(out)
           count += 1
print_fibonacci()