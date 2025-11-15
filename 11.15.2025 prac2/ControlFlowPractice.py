'''1.
a = 6
b = 2
c = 4

if a % b == 0:
    if c * 2 == a:
        print("X")
    elif c + b == a:
        print("Y")
    else:
        print("Z")
else:
    print("W")'''

# Y

'''2. 
if (x % 4 == 0 or x - 3 < 10) and (x // 2 != 7):
    print("YES")'''

#25 and 14

'''3. 
a = 5
b = 12
if (a * 2 == b - 2) or (b % a == 0):
    if b // a < 3:
        print("ONE")
    else:
        print("TWO")
else:
    print("THREE")'''

#ONE

'''4. 
x = 9
y = 4
z = 6

if (x + y > z * 2) and not (y * 2 == z):
    if (x % y < z // 2):
        print("A")
    elif (x - z == y):
        print("B")
    else:
        print("C")
else:
    print("D")'''

#A

'''5.
a = 7
b = 3
c = 10

if (a > b and c % a != 3) or (b * 2 == a - 1):
    if (c // b == a - b):
        if (a + b + c) % 2 == 0:
            print("X")
        else:
            print("Y")
    elif (a * b > c):
        print("Z")
    else:
        print("W")
else:
    print("Q")'''

#Z

'''6.
fruits = ["apple","pear","pineapple"]
for fruit in fruits:
    print(fruit)'''

#apple pear pineapple

'''7.
i = 2
while True:
    if i > 8:
        break
    if i % 2 == 0:
        print(i)
    i += 3'''

#2 8

'''8.
i = 10
while True:
    if i % 4 == 0:
        print(i)
        break
    i -= 3'''

#4

'''9.
x = 1
while x < 10:
    x += 3
    print("*", end="")
else:
    print("*")'''

#***

'''10.
i = 7
while i > 0:
    if i % 2 == 1:
        print("*", end="")
    else:
        print("*")
        break
    i -= 3
else:
    print("*")'''

#**

'''11.
t = 1
while t < 50:
    print("*", end="")
    if t % 4 == 0:
        print("*", end="")
    t *= 3
else:
    print("*")'''

#*****