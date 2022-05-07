# Q-1 Write a Python program to find those numbers which are divisible by 7and multiple of 5, between 1500 and 2700 (both included).


# enter the starting range number
start_num = int(1500)

# enter the ending range number
end_num = int(2700)

# initialise counter with starting number
cnt = start_num

# check until end of the range is achieved
while cnt <= end_num:
	
	# if number divisible by 7 and 5
	if cnt % 7 == 0 and cnt % 5 == 0:
		print(cnt, " is divisible by  5.")
		

	# increment counter
	cnt += 1


#Q-2 Python program to add two numbers
  # This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#Q3-Maximum of two numbers in Python
# Python program to return maximum of two numbers

# Python program to return maximum of two numbers

# Getting input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# printing the maximum value
if(num1 > num2):
  print(num1, "is greater")
elif(num1 < num2):
    print(num2, "is greater")
else:
    print("Both are equal")
    
#Q-4 Python Program for factorial of a number
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
#Q-5 write a python programme for simple interest

P = 1000
R = 1
T = 2
# simple interest
SI = (P * R * T) / 100
print("simple interest is", SI)

#Q-6 write a python programme for compound interest
#define principal, interest rate, compounding periods per year, and total years
P = 5000
r = .06
n = 1
t = 10

#calculate final compound interest
P*(pow((1+r/n), n*t))


#Q-7 Python Program to check Armstrong Number

# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Q-8 Python Program for Program to find area of a circle
# Python program to find Area of a circle
  
def findArea(r):
    PI = 3.142
    return PI * (r*r);
  
# Driver method
print("Area is %.6f" % findArea(5));

#Q-9 Python program to print all Prime numbers in an Interva
# Python program to print all
# prime number in an interval
 
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)

#Q-10 Python program to check whether a number is Prime or not
# Python program to check if
# given number is prime or not
  
num = 11
  
# If given number is greater than 1
if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")






