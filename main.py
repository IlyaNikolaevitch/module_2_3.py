first = 35
second = 75
third = 35
if first == second and first == third and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)