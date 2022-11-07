def str_slicing_operations():
    print("Enter a string value:")
    str_val=input()
    print("You entered : '{0}'".format(str_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first and last character '{0}' " .format(str_val[1:-1],str_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing first 2 character '{0}' " .format(str_val[2:],str_val))
    print("--------------------------------------------")
    print("Slice of '{1}' after removing  last 2 character '{0}' " .format(str_val[:-2],str_val))
    print("--------------------------------------------")
    mid_index=len(str_val)//2
    print("Mid index is '{0}'" .format(mid_index))
    print("--------------------------------------------")
    print("First half slice of '{1}' is {0} is".format(str_val[:(len(str_val)) // 2],str_val))
    print("Second half slice of '{1}' is '{0}'". format(str_val[(len(str_val))//2:],str_val))

str_slicing_operations()
