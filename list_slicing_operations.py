def lst_slicing_operations():
    lst_val = int(input("Enter number of elements to insert into the list: "))
    lst_val = list(map(int, input("\nEnter the numbers separated by comma(ex: 222,55,77) : ").strip().split(',')))[
              :lst_val]
    print("You entered : '{0}'".format(lst_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first and last items '{0}' " .format(lst_val[1:-1],lst_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first 2 items '{0}' " .format(lst_val[2:],lst_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing  last 2 items '{0}' " .format(lst_val[:-2],lst_val))
    print("--------------------------------------------")
    mid_index=len(lst_val)//2
    print("Mid index is '{0}'" .format(mid_index))
    print("--------------------------------------------")
    print("First half slice of '{1}' is {0} is".format(lst_val[:(len(lst_val)) // 2],lst_val))
    print("Second half slice of '{1}' is '{0}'". format(lst_val[(len(lst_val))//2:],lst_val))

lst_slicing_operations()
