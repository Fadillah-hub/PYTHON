x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

#int
a = 1
b = 35656222554887711
c = -3255522
print(type(a))
print(type(b))
print(type(c))

#float
d = 1.1
e = 2.8
f = -32.55522
print(type(d))
print(type(e))
print(type(f))

#complex
g = 1j
h = 3 + 5j
print(type(g))
print(type(h))

#type conversion
i = 1
j = 2.8
k = 1j

a = float(i) #convert from int to float
b = int(j) #convert from float to int
c = complex(i) #convert from int to complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random number
import random
print(random.randrange(1, 10))