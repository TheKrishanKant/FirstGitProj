'''a = "hello, Mr. Krishan"
print(a.count("ri"))
print(a.capitalize())
print(a.center(80))
print(a.encode())
print(type(a))
print(a.find("n"))
print(a.isalnum())
print(a.isalpha())
print(a[::-1])
'''


# b = {}
# b["Krishan"] = "Topper"
# print(b)
# b["Vaibhav"] = "Peak"
# b["Subhanshu"] = "Not clearly known"
# print(b)
# b["new dict"]= {"i": "ice cream", "j" : "joker", "k" : "kite", "l" : "lemon"}
# print(b)
# d = b.copy()
# del b["Krishan"]
# print(b)
# c = b
# del c["Vaibhav"]
# del d["Subhanshu"]
# print(b)
# print(d)
# print(b.get("Subhanshu"))
# b.update({"Henry" : "Clever"})
# print(b)
# print(b.keys())
# print(b.items())
# print(b.values())
# print(d["new dict"]["j"])


'''
e = [1, 2, 3, 4, 5]
f = set(e)
print(type(f))
print(f)
print(max(f))
print(min(f))
f.add(6)
print(f)
g = set([5, 6, 7, 8, 8, 9])
print(g)
print(f.intersection(g))
print(f.union(g))
f.remove(4)
print(f)
print(f.isdisjoint(g))
'''



# list1 = [["Krishan Kant", 100], ["Himanshu", 10], ["Sonu", 40], ["Vansh Rawat", 60],
# ["Aman Bhagat", 35], ["Harshit Rawat", 25]]
# print(list1[0],",", list1[1])
# print(list1[0:2])
# for i in list1:
#     print(i)
# for i, j in list1:
#     print(i ,"'s score is: ", j)
#     if j>=50:
#         print(j,"Amazing is'nt it")
#     else:
#         print(j, "Really, Sorry to say not so great")





# list1 = [["Krishan Kant", 100], ["Himanshu", 10], ["Sonu", 40], ["Vansh Rawat", 60],
# ["Aman Bhagat", 35], ["Harshit Rawat", 25]]
# dict1 = dict(list1)
# print(dict1)
# print(dict1.values())
# for items in dict1:
#     print(items)
# for key, value in dict1.items():
#         #print(key)
#         #print(value)
#         print(key, value, end=", ")





# i = 0
# j = 0
# while(i<=20):
#     print(i)
#     i = i + 2
# while(True):
#     print(j, end= " ")
#     if (j == 20):
#         break
#     j = j+1





# i = 0
# while(True):
#     if i<10:
#         i = i + 1
#         continue
#     print(i+1, end= " ")
#     if i == 19:
#         break
#     i = i + 1


'''
listk = []
listk.append("Krishan Kant")
listk.append("Me")
listk.append("myself")
listk.pop()
print(listk)
listk.remove("Krishan Kant")
print(listk)
print(len(listk))
'''

#airthematic operator (+,-,/,*,   //floar division point se phle ka dega,  %remainder,  ** modulus,)
#assignment operator (=, += number jod dega ,  /=,  -=,  %=)
#comparison operator (==,  <,  >,  >=,  <=)
#logical operator (Ture, False)
#identity operator (is,  is not)
#membership operator (in ,  not in)
#bitwise operator (1, 0)
#0 - 00
#1 - 01
#2 - 10
#3 - 11

# and = &,  or = |


# print(0 | 3)
# x = 5
# x %= 4
# print(x)
# a = [1, 2, 3, 4, 5, 6]
# print(2 in a)
# print(8 not in a)

'''
#short hand if else
a = int(input())
b = int(input())
print("A i bigger") if a>b else print("B is greater")
'''

# print(sum((4,5)))
# #sum(())   2 brackets hai     built in function

'''
def funct(a,b):
    """ This function calculate the average of two numbers. """
    c = (a+b)/2
    return c
print(funct.__doc__)
print(funct(5,9))
'''


# a = input()
# b = input()
# try:
#     print(int(a)+int(b))
# except Exception as e:
#     print("Oh! Man", e)
# print("What's Up, New York")


'''
'r' = open file for reading
'w' = open file for writing
'x' = creates a file if does not exist
'a' = add more content to a file
't' = text mode
'b' = binary mode
'+' = read and write
'''


# f = open("KK.txt", "r+")
# a = f.read()
# b = f.read(10)
# c = f.read()
# print(a, b, c)
# for line in f:
#     print(line, end = "")
# for line in a:
#     print(line, end = "")
# print(f.readline())
# print(f.readlines())
# d = f.write("He is the best, no doubt")
# f.write("\n")
# f.write("I am talking about Mr. Krishan Kant \n")
# f.write("We call him KK")

# f = open("KK.txt", "r+")
# print(f.read())
# f.write("\n He is one of the brilliant minded person")
# f.close()


# f = open("KK.txt", "r+")
# print(f.tell()) #tell where the pointer is on which character
# print(f.readline())
# print(f.tell())
# print(f.seek(10)) # brings the pointer to the character
# print(f.tell())
# print(f.readline())


# f = open("file name")
# f.close() in dono line ki jagah hum keval
# with open("file name", mode) as f:
#     likh sakte hai close khud hi kar deta hi isme

# with open("KK.txt", "rt") as f:
#     print(f.readlines())


# f = open("KK.txt", "rt")
# print(f.readline())
# print(f.readline())
# f.close()

# l = 10
# def funtion_1():
#     m= 15
#     global l
#     l = l+10
#     print("L is updated", l, m+15)
# funtion_1() #no error as we have written global l and if not written then it will give error


# def krish():
#     x = 20
#     def an_kant():
#         global x
#         x = 45
#     print("Before calling an_kant, x is:", x)
#     an_kant()
#     print("After calling an_kant, x is:", x)
# krish()
# # This code demonstrates the use of global variables and nested functions.
# print("After calling krish, x is:", x)
# #global means outside of the function ekdum bahar
# #thats why first two x gives 20


# def factorial_iterative(n):
#     """Calculate factorial of n using an iterative approach."""
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("Enter a number to find its factorial: "))
# print("Factorial of that number using iterative method", factorial_iterative(number))


# def fatorial_recursive(m):
#     """Calculate factorial of n using a recursive approach."""
#     if m == 0:
#         return 1
#     else:
#         return m * fatorial_recursive(m-1)
# number = int(input("Enter a number to find its factorial: "))
# print("Factorial of that number using recursive method", fatorial_recursive(number))
    






