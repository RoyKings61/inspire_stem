# programme to calculate factorials
# Date : 20/02/2024
# Name : Roy Kings

num = int(input("Enter a number to find the factorial: "))
count = 1
for i in range(1,num+1):
    count *= i

print(count)