def greeting(name):
  print("Hello, " + name)

# using a module 
import Modules

Modules.greeting("Jonathan")

# variables in module
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import Modules

a = Modules.person1["age"]
print(a)

# renaming a module
import Modules as mx

a = mx.person1["age"]
print(a)

#  built in modules
import platform

x = platform.system()
print(x)

#sing the dir() function
import platform

x = dir(platform)
print(x)

# import from module 
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from Modules import person1
print (person1["age"])

