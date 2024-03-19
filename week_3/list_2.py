friends = ["Roy","Kings","joel","joy","gojo","naruto"]
for friends in friends:
   print(friends)

   enemies = friends[:] # to copy one list to another
   
   print(enemies)


fruits = ("mango","apple","peach","guve","orange")

   #slice the list ie get part of the list
print(fruits[0.3])


del fruits[0]

print(fruits)

squares = []# initialize an empty list

for x in range(0,11):
   squares.append(x**2)
   print(squares)