def tuple_slicing_operations():
    tup_val = tuple(input("\nEnter the numbers separated by comma(ex: 222,55,77) : ").split(','))
    print("You entered : '{0}'".format(tup_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first and last items '{0}' " .format(tup_val[1:-1],tup_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first 2 items '{0}' " .format(tup_val[2:],tup_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing  last 2 items '{0}' " .format(tup_val[:-2],tup_val))
    print("--------------------------------------------")
    mid_index=len(tup_val)//2
    print("Mid index is '{0}'" .format(mid_index))
    print("--------------------------------------------")
    print("First half slice of '{1}' is {0}".format(tup_val[:(len(tup_val)) // 2],tup_val))
    print("Second half slice of '{1}' is '{0}'". format(tup_val[(len(tup_val))//2:],tup_val))

tuple_slicing_operations()