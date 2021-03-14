import math

a = float(input("Enter wigth1"))
b = float(input("Enter wigth2"))
c = float(input("Enter wigth3"))

result1 = b + c
result2 = a + c
result3 = a + b


if a < result1 and b < result2 and c < result3:
    print("you can create triangle")
else:
    print("you can't create triangle")
