a = int(input("Enter your age: "))
if a <= 7 or a >= 100:
    print("You should stay at home and forget abnout driving")
elif 7 < a < 18:
    print("No, You cannot drive")
elif a == 18:
    print("you need to visit RTO")
else:
    print("Yes, You can drive")
