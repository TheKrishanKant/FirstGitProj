#make a list and print only number which is greater than 6
list1 = ["a", "45", 46, 15, 3, 6, "kk"]
for i in list1:
    if str(i).isnumeric() and int(i) > 6:
        print(i)
