# Programme to solve quadratic equations
# Date : 20/02/2024
# Name : Roy Kings

a =float (input(" enter coefficient of first term: "))
b = float(input (" enter coefficient of second term: "))
c =float( input("enter constant: "))

d = float(((b)**2) - 4 * (a) * (c))

x_1 =( (-b + math.sqrt(d)) / 2 * a)
x_2 =( (-b - math.sqrt(d)) / 2 * a)

print("The solution of the quadratic equation is :", x_1)
print("The solution of the quadratic equation is :", x_2)