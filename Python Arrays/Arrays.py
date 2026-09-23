cars = ["Ford", "Volvo", "BMW"]

#access the elements of an array
x = cars[0]
cars[0] = "Toyota"

# the length of an array
x = len(cars)

#looping array elements
for x in cars:
  print(x)
  
#adding array elements
cars.append("Honda")

#removing array elements
cars.pop(1)

cars.remove("Volvo")