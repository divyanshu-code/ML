# Q.01 - write a program that ask a user for their name and age , then prints a sentence like "Hello [name], you are [age] years old."

# name = input("please enter your name:")
# age = input("please enter you age: ")

# print(f"Hello {name} , you are {age} years old!")

# Q.02 - take a two numbers as input from the user and print their sum , differnece , product , and quotient.

# firstNumber = float(input("Enter a first no.: "))
# secondNumber = float(input("Enter a second no.: "))

# print("Sum is: ", firstNumber + secondNumber)
# print("Difference is: ", firstNumber - secondNumber)
# print("Product is: ", firstNumber * secondNumber)
# print("Quotient is: ", firstNumber / secondNumber)

# Q.03 - Ask a user to enter two integers and one float . convert them all to floats and print their average.

# firstNumber = float(input("Enter a first no.: "))
# secondNumber = float(input("Enter a second no.: "))
# thirdNumber = float(input("Enter a third no.: "))

# finalAnswer = (firstNumber+secondNumber+thirdNumber)/3 
# print("Average is: " , finalAnswer)

# Q.04 

# value = input("enter the string: ")

# integer= int(value) 
# print("convert  into integer" , type(integer))

# integer= float(value) 
# print("convert into float" , type(integer))

# integer= str(value) 
# print("convert  into string" , type(integer))

# Q.05 

# x = 10 + 3 * 2 ** 2

# print("Answer is: " , x)

# reason :- python solve the expression based on operator precedence . In this expression power ( ** ) operator will excecute first , then mulitply and the addition. 

# 1--> 2 ** 2 = 4 
# 2--> 3 * 4 = 12 
# 3--> 10 + 12 = 22

# Q.06 

# firstNumber = float(input("Enter a first no.: "))
# secondNumber = float(input("Enter a second no.: "))

# finalNumber = firstNumber
# firstNumber = secondNumber
# secondNumber = finalNumber

# print("Firstnumber: " , firstNumber)
# print("Secondnumber: " , secondNumber)

# Q.07 

# tempt= input("Enter a temperature in celcius: ")

# temperature = int(tempt)

# conversion = (temperature * (9/5)) + 32
# print("Temperature in Fahrenheit: " , conversion)

# Q.08

# radius= float(input("Enter the radius: "))

# areacalculation = 3.14 * radius ** radius

# print("Area of circle: " , areacalculation)

# Q.09 

# P= float(input("Enter the principle: "))
# R= float(input("Enter the rate: "))
# T= float(input("Enter the time: "))

# SI = (P*R*T)/100 

# print("Simple interest: " , SI)

# Q.10 

value= float(input("Enter the value: "))

integer = int(value)
floating = float(value)

print("Integer part: " , integer)
print("Floating part: " , floating-integer)