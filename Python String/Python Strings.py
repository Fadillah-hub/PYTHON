print("Hello")
print("It's a alright")

a ="Hello"
print(a)

b = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(b)

#string are arrays
h = "Hello, World!"
print(h[1])  # Output: H

#looping throught a string
for x in "banana":
  print(x)
  
#string length
s = "Hello, World!"
print(len(s))

#check string
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")  
    
#check if not in string
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
