def lst_slicing_operations():
    lst_val = ["Apple", "Orange", "Kiwi", [1, 2, 3]]
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
