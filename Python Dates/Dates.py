import datetime

x = datetime.datetime.now()
print(x)

# date output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# creating data objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# thesttrftime() method
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
