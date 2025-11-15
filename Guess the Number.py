n = 1168
a = []
b = 10
andd = "And"
print("You have to guess the number")
print(andd.center(20))
print("You Have Only 10 Tries \n")
print("Hint: It is between 1000 and 2000 \n")
while(True):
    i = int(input("Enter the Number: "))
    if i < n:
        print("Guess Greater \n")
        a.append(i)
        b = b-1
        print(b ,"tries left \n")
        if b == 0:
            print("You Lost")
            break
        continue
    elif i > n:
        print("Guess Smaller \n")
        a.append(i)
        b = b-1
        print(b ,"tries left \n")
        if b == 0:
            print("You Lost")
            break
        continue
    else:
        print("Correct You Won \n")
        a.append(i)
        print("You took", len(a), "tries.")
        b = b-1
        break
