def lst_ind_operations():
    lst_val=["Apple","Orange","Kiwi",[1,2,3]]
    print("You entered : '{0}'".format(lst_val))
    print("--------------------------------------------")
    print("First item in '{1}' is '{0}' " .format(lst_val[0],lst_val))
    print("--------------------------------------------")
    print(len(lst_val))
    lst_str = len(lst_val) -1
    print("Last item in '{1}' is '{0}'" .format(lst_val[lst_str],lst_val))
    print("--------------------------------------------")
    print("Length of list  '{1}' is  '{0}'" .format(len(lst_val),lst_val))
    print("--------------------------------------------")
    mid_index=len(lst_val)//2
    print("Mid index is '{0}'" .format(mid_index))
    print("--------------------------------------------")
    # if the string is even then return two character otherwise one character
    print("Middle Character in '{1}' is/are {0}". format(lst_val[(len(lst_val)-1)//2:(len(lst_val)+2)//2],lst_val))

lst_ind_operations()