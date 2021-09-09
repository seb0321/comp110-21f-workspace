is_rainy: bool = True
is_cold: bool = False
print(not is_rainy)
print(not is_cold)
print(not True)
print(is_rainy and is_cold)
print(is_rainy or is_cold)

is_cold = True 
print (is_rainy or is_cold)
print(is_rainy and is_cold)

if is_rainy and is_cold:
    print ("bring a jacket!")
else:
    print("Don't bring a jacket!")

age: int = 19
height: float = 6.1
if age > 18 and height >= 5.0:
    print("You can ride")
else:
    print("Try the tea cups ride")

age: int = 11
if age > 18 and height >= 5.0:
    print("You can ride")
else:
    print ("You can't ride")

can_ride: bool = age > 19 and height >= 5.0
print(can_ride)

age: int = 21
can_ride = age > 18 and height >= 5.0
print(can_ride)





