# Q.01 ---------------------------------------------------------------------------------------------

# salary = int(input("Enter the salary: ")) 

# if(salary < 30000):
#     print("5%")
# elif(salary >= 30000 and salary <= 70000):
#     print("15%")
# else:
#     print("25%")

# Q.02 ---------------------------------------------------------------------------------------------

# def printeven(a , b):
#  if(a%2==0):
#   for a in range(a,b+1,2):
#       print(a)
#  else:
#    for a in range(a+1,b+1,2):   
#       print(a)

# a = int(input("Enter the value a: ")) 
# b = int(input("Enter the value b: ")) 
# printeven(a,b)

# Q.03 ---------------------------------------------------------------------------------------------

# def printdigit(n):
#    digit= 0
#    while(n>0):
#       digit = n // 10
#       print(digit)
#       n = n %10

# a = int(input("Enter the value: ")) 
# printdigit(a)

# Q.04 ---------------------------------------------------------------------------------------------

# def printdigit(n):
#    count= 0
#    while(n>0):
#       count = count+1 
#       n = n // 10

#    print(count)

# a = int(input("Enter the value: ")) 
# printdigit(a)

# Q.05 ---------------------------------------------------------------------------------------------

# def printdigit(n):
#    sum= 0
#    while(n>0):
#       sum += n%10 
#       n = n // 10

#    print(sum)

# a = int(input("Enter the value: ")) 
# printdigit(a)

# Q.06 ---------------------------------------------------------------------------------------------

# for i in range(1,100,1):
#     if(i %3 ==0 and i%5 == 0):
#         print(i)

# Q.07 ---------------------------------------------------------------------------------------------

# while(True):
#   num = input("Enter the number: ")

#   if(num == 'Quit'):
#      break
#   else:
#      print(num)

# Q.08 ---------------------------------------------------------------------------------------------

# def calculator(a , b , operator):
#     if(operator == '+'):
#        return a+b;
#     elif(operator == '-'):
#        return a-b
#     elif(operator == '*'):
#        return a*b
#     elif(operator == '/'):
#        return a/b
#     else:
#        return a%b 

# firstNumber = int(input("Enter the firstNumber: "))
# secondNumber = int(input("Enter the secondnNumber: "))
# operator = input("Enter the operator(+ , _ , * , /): ")

# print(calculator(firstNumber, secondNumber, operator))

# Q.09 ---------------------------------------------------------------------------------------------

# def is_prime(n):
#     count =1
#     for i in range(2,n+1,1):
#         if(n % i ==0 ):
#             count += 1
    
#     if(count == 2):
#         return True
#     else:
#         return False

# n = int(input("Enter the number: "))
# print(is_prime(n))

# Q.10 ---------------------------------------------------------------------------------------------

preNo = 20

while(True):
 n = int(input("Enter the number: "))

 if(n > preNo):
   print("Number is Too high")
 elif(n < preNo):
   print("Number is Too low")
 else:
   print("You guess the right Number")
   break