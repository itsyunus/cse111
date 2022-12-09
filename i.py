

import math

_user_shape=input('What is the shape you want to find area(cube/cylinder/triangle): ')

if _user_shape=="cube":
    def find_surafce_area(l, b, h):
        Surface_area = 2 * ( l * b + b * h + h * l)
        print("Surface_area: ",Surface_area)
    def find_volume(l, b, h):
        Volume = (l * b * h)
        print("volume: ",Volume)
    def find_space_diagonal(l, b, h):
        Space_diagonal = math.sqrt(l**2 + b**2 + h**2)
        print("space_diagonal: ",Space_diagonal)
    l=int(input('length: '))
    b=int(input('breath: '))
    h=int(input('height: '))
    find_surafce_area(l, b, h)
    find_volume(l, b, h)
    find_space_diagonal(l, b, h)
	
if _user_shape=="cylinder":
    pi=22/7
    height = float(input('Height of cylinder: '))
    radian = float(input('Radius of cylinder: '))
    volume = pi * radian * radian * height
    sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
    print("Volume is: ", volume)
    print("Surface Area is: ", sur_area)

if _user_shape=="triangle":
    def volumeTriangular(a, b, h):
        return (0.1666) * a * b * h
    def volumeSquare(b, h):
        return (0.33) * b * b * h
    def volumePentagonal(a, b, h):
        return (0.83) * a * b * h
    def volumeHexagonal(a, b, h):
        return a * b * h
    b = float(input('breath of triangle: '))
    h = float(input('height of the triangle: '))
    a = float(input("weith of the triangle: "))
    print( "Volume of triangular base pyramid is ",
					volumeTriangular(a, b, h) )
    print( "Volume of square base pyramid is ",
					volumeSquare(b, h) )
    print( "Volume of pentagonal base pyramid is ",
					volumePentagonal(a,b, h) )
    print( "Volume of Hexagonal base pyramid is ",
					volumeHexagonal(a, b, h))

