x = range(10)

# call range() w/ two arguments
x = range(3, 10)

# w/ three arguments
x = range(3, 10, 2)

# using ranges
for i in range(10):
  print(i)

# using list to display ranges
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

#slicing ranges
r = range(10)
print(r[2])
print(r[:3])

# membership testing
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# length
r = range(0, 10, 2)
print(len(r))