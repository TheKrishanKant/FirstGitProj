print("Enter the numbers: ")
a = int(input())
b = int(input())
c = input("Enter the Operator: ")
if c == "+":
    if (a, b) == (56, 9) or (a, b) == (9, 56):
        print(77)
    else:
        print(a+b)
elif c == "*":
    if (a, b) == (45, 3) or (a, b) ==  (3, 45):
        print(555)
    else:
        print(a*b)
elif c == "/":
    if (a, b) == (56, 6):
        print(4)
    else:
        print(a/b)
elif c == "-":
    print(a-b)
else:
    print("You can only choose operator from this (+,-,*,/)")
