#!/usr/bin/python3
for num in range(0, 100):
    if num >= 0 and num <= 9:
        num = str(num).zfill(2)
    print("{}".format(num), end=", ")
print("")
