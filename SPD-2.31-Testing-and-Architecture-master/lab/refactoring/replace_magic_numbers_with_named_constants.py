# by Kami Bigdely 
# Replace magic numbers with named constanst

xVal = 1e9
forceConstant = 8.987551923
# First Section
# Given two point charges, calcualte the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))
force = forceConstant*xVal * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")
# Second Section

TWO = 2
ZERO = 0


num = int(input('Enter an integer number: '))
if num % TWO == ZERO:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")