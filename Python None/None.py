x = None
print(x)

x = None
print(type(x))

# comparing to none
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

# true of false
print(bool(None))

# functions returning none
def myfunc():
  x = 5

x = myfunc()
print(x)
