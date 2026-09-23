# Create the i variable
i = 1

# While loop: print 1-5, skip 3 with continue
while i <= 5:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1