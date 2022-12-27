#take input of three sides of triangle

p = float(input('Enter first side of triangle: '))
q = float(input('Enter second side of triangle: '))
r = float(input('Enter third side of triangle: '))

#calculate the semi perimeter

semiPerimeter = (p+q+r)/2

#calculate the area

areaofTriangle = (semiPerimeter*(semiPerimeter-p)*(semiPerimeter-q)*(semiPerimeter-r))**0.5

print("Area of Triangle with given sides is ", areaofTriangle)
