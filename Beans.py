# list1 = ["Beans", "Bean", "Bean Except Large", "asd", "adwadw"]
# del list1[2]
# print(list1)
import random
p = 0
p = random.randint(5, 10)
print (p)
list2 = []
for x in range (0, p):
    list2.insert(1, "1")
print(list2)
if len(list2) == 6 or len(list2) == 8 or len(list2) == 10:
    list2.insert(0, "even")
    print(list2)
elif len(list2) == 5 or len(list2) == 7 or len(list2) == 9:
    list2.insert(0, "odd")
    print(list2)
for x in range (0,4):
    b = "b"
    print(b)
    e = "e"
    print(e)
    a = "a"
    print(a)
    n = "n"
    print(n)

h = "Your A Wizard Harry"
print(h)
h = h.replace("o" or "O","0")
print(h)
h = h.replace("h" or "H","4")
h = h.replace("e" or "E","3")
print(h)


print("Racecar")
print("racecaR")