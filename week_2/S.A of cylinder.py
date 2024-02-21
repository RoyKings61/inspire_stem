# simple programe to find surface area of a cylinder
# date : 20/02/2024
# Name : Roy Kings

p = float (3.142)
r = float(input("enter radius value"))
d = float(r * 2)
h = float(input("enter height value"))

x = float((p*r**2 *2) + p * d * h)
print("surface area of a cylinder is :", x)