def str_ind_operations():
    print("Enter a string value:")
    str_val=input()
    print("You entered : '{0}'".format(str_val))
    print("--------------------------------------------")
    print("First Character in 'Hello' is '{0}' " .format(str_val[0]))
    print("--------------------------------------------")
    print(len(str_val))
    lst_str = len(str_val) -1
    print("Last Character in 'Hello' is '{0}'" .format(str_val[lst_str]))
    print("--------------------------------------------")
    print("Length Character in 'Hello' is  '{0}'" .format(len(str_val)))
    print("--------------------------------------------")
    mid_index=len(str_val)//2
    print("Mid index is '{0}'" .format(mid_index))
    print("--------------------------------------------")
    # if the string is even then return two character otherwise one character
    print("Middle Character in 'Hello' is/are {0}". format(str_val[(len(str_val)-1)//2:(len(str_val)+2)//2]))

str_ind_operations()
