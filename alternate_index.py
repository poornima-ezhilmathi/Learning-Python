def print_character():
    print("Enter a number:")
    val = input()
    for c in val:
        #print(val.index(c))
        ind=val.index(c)
        if ind %2 ==0:
            print(c)
            continue


print_character()