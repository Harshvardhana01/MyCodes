#Oreiginal
#Findin the root of a Quadric Equation

#-b+squarroot of (b*b-(4*a*c))/(2*a)
#-b-squarroot of (b*b-(4*a*c))/(2*a)

import math
a = int(input('Enter Value of a:'))
b = int(input('Enter Value of b:'))
c = int(input('Enter Value of c:'))

d = math.pow(b,2)*(4*a*c)

if d>0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    
    print("Roots are real and unequal",r1, " and ",r2)
elif d==0:
    print("Roots arereal and same",r1)
else:
    print("No real roots found")
