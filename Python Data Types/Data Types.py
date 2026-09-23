x = 5
print(type(x))

#Setting the data type
x = "Hello, World!"  # x will be <class 'str'>
y = 20              # y will be <class 'int'>
z = 20.5            # z will be <class 'float'>
a = 1j              # a will be <class 'complex'>
b = ["apple", "banana", "cherry"]  # b will be <class 'list'>
c = ("apple", "banana", "cherry")  # c will be <class 'tuple'>
d = range(6)        # d will be <class 'range'>
e = {"name" : "John", "age" : 36}  # e will be <class 'dict'>
f = {"apple", "banana", "cherry"}  # f will be <class 'set'>
g = frozenset({"apple", "banana", "cherry"})  # g will be <class 'frozenset'>
h = True            # h will be <class 'bool'>              
i = b"Hello"       # i will be <class 'bytes'>
j = bytearray(5)   # j will be <class 'bytearray'>
k = memoryview(bytes(5))  # k will be <class 'memoryview'>
l = None           # l will be <class 'NoneType'>
