def print_name():
    print("my name is Roy")

#calling the fuction
print_name()    
print_name() 
print_name() 
print_name() 


def print_details(name , age , id , gender):
 print("i am {0} , i am {1} , my id no is {2} , i am {3}".format(name , age , id , gender))

print_details("Roy Kings" , "20" , "123456789" , "male")
print_details("Joy faith" , "20" , "123456789" , "female")

def sum_nums(x,y):
   return x+y

z = sum_nums(10,20)
print(z)

def prod_nums(m,n):
   return m * n

print(prod_nums(3,4))

# how to use for lop inside a fuction

def print_odds(frist_nums , last_nums):
   for i in range(frist_nums , last_nums):
      print(i %3 )

print_odds(0,15)      