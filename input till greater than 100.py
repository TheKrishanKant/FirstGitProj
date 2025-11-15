list1 = []
while(True):
    i = int(input())
    if i <= 100:
        print("Dude! Think Bigger\n")
        list1.append(i)
        a = len(list1)
        continue
    print("Congratulations, Finally you thought something bigger than 100\n")
    print("But it took you ", a+1, "tries to think this much\n")
    list1.append(i)
    print("Your Enteries: ", list1)
    break

