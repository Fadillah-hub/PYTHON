x = "awesome"

def myfunc():
    print("Python is " + x)
    
myfunc()

print("Python is " + x)

#the global keyword
def myfunc():
    global x
    x = "fantastic"
    
myfunc()
print("Python is " + x)
