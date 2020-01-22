# CSC 110 - Spring 2016 - Section 1
# Week 5 (Accessing Data from Files) - Class Activities (Tuesday)
# Exercise 1


Def daddy(num):
    g = num + 23
    return g

Def happy(r):
    print("I Have ", r, "toys in my crib")
    
Def baby():
    print("I am 14 months old")
    print("I can only speak baby words")
    print("please don't laugh at me!")

Def yummy(s1, s2):
    if (s1 >= s2):
        return (s1 - s2)
    else:
        return (s2 - s1)

Def sleepy(wakehours):
    if(wakeHours > 4):
        return True
    else:
        return False

Def bootie(a,b,c):
    s = 1
    s = s + a
    s = s * b
    s = s / c
    return int(s)

Def mommy(k):
    b = k * 5
    b = b - 1
    return b

# Start of main program:
w = 10
x = 7
y = 29
z = 4
baby()
a1 = daddy(10)
print("My daddy is: ", a1, " years old")
a2 = mommy(x)
print("I have only 4 teeth")
print("But mommy has: ", a2, "teeth")
print("I am happy today!")
happy(x - z)
a3 = bootie(33, 10, a2)
print("The size of my bootie is: ", a3/2)
print("When I am hungry, I drink: ", yummy(x,z), "bootles of milk")
playHours = 6
if sleepy(playHours):
   print('Time for bed!')
else:
   print('I want to play more!')
# End of main program

