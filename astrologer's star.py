n = int(input("Enter the interger: "))
m = int(input("Enter 0 or 1: "))
o = bool(m)
if o == True:
    x = 0
    while (x < n):
        print("*"*(x+1))
        x= x+1
else:
    y = 0
    while(y < n):
        print("*"*(n-y))
        y = y + 1