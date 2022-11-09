def with_continue():
    print("Enter a number:")
    val = input()
    i = 1
    for c in val:
        #print(val.index(c))
        #ind=val.index(c)
        if i %2 ==0:
           i = i + 1
           #print(c)
           continue
        print(c)
        i = i+1

def with_break():
    print("Enter a number:")
    val = input()
    i = 1
    for c in val:
        #print(val.index(c))
        #ind=val.index(c)
        if c == 'z':
           i = i + 1
           #print(c)
           break
        print(c)
        i = i+1

with_continue()
with_break()