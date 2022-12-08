def tuple_indexing_operations():
    tup_val = tuple(input("\nEnter the numbers separated by comma(ex: 222,55,77) : ").split(','))
    print("You entered : '{0}'".format(tup_val))
    print("You entered : '{0}'".format(tup_val))
    print("--------------------------------------------")
    print("First item in '{1}' is '{0}' ".format(tup_val[0], tup_val))
    print("--------------------------------------------")
    #print(len(tup_val))
    lst_str = len(tup_val) - 1
    print("Last item in '{1}' is '{0}'".format(tup_val[lst_str], tup_val))
    print("--------------------------------------------")
    print("Length of list  '{1}' is  '{0}'".format(len(tup_val), tup_val))
    print("--------------------------------------------")
    mid_index = len(tup_val) // 2
    print("Mid index is '{0}'".format(mid_index))
    print("--------------------------------------------")
    # if the string is even then return two character otherwise one character
    print("Middle Character in '{1}' is/are {0}".format(tup_val[(len(tup_val) - 1) // 2:(len(tup_val) + 2) // 2],
                                                        tup_val))

tuple_indexing_operations()