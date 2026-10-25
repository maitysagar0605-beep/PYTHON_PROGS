#print ("hello world")

#name = input("Enter Your name:")
#print(f"WELCOME TO THE WORLD OF PYTHON, {name}!!")

#BASIC USER INPUT
"""age = int(input("Enter Your Age:"))
print(f"Next Year you Will Be {age+1} Years Old")"""

#SUM OF TWO NUMBERS WITH USER INPUT
"""n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
print(f"Sum of the two numbers is: {n1 + n2}")"""

#FACTORIAL OF A NUMBER
"""n = int(input("Enter a Number:"))
fact = 1
while n>0:
    fact *= n
    n-=1
print(f"Factorial of the Number is : {fact}")"""    

#PALINDROME NUMBER OR NOT & REVERSE OF A NUMBER WITH USER INPUT
"""n = int(input("Enter a +ve Number:"))
num = n
rev = 0
while num>0:
 digits = num % 10
 rev = rev*10 + digits
 num//=10
print(f"Reverse of the number is: {rev}")
if n==rev:
 print("The number is a palindrome number")
else:
  print("The number is not a palindrome number")""" 

#COUNT NUMBER OF DIGITS OF USER INPUTED NUMBER
"""n = 1234
while n > 0:
    digits = n%10
    n//=10
    print(digits)"""

#ARMSTRONG NUMBER OR NOT WITH USER INPUT
"""num = int(input("Enter a number: "))
temp=num

num_str=str(num)
power=len(num_str)

sum=0

while temp>0:
    digits=temp%10
    sum= digits ** power+ sum
    temp//=10
if sum==num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")"""

#LEAP YER OR NOT CHECK
"""year=int(input("Enter a year: "))

if(year%100!=0 and year%4==0 or year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")"""

#FIBONACCI SERIES
"""n=int(input("Enter number of terms: "))

n1,n2=0,1
count=0

while count<n:
    print(n1, end=" ")
    new=n1+n2

    n1=n2
    n2=new
    count+=1
print()"""

#FIBONACCI SERIES WITH LIMIT
"""limit=int(input("Enter the extreme limit(N): "))

a,b=0,1

print(f"Fibonacci series under {limit}:")
while a<limit:
    print(a, end=" ")
    a,b=b,a+b
print()"""

#PRIME NUMBER FINDING WITH USER INPUT
"""import math
n= int(input("Enter a number: "))
r= int(math.sqrt(n))

is_Prime=True
if n<=1:
    is_Prime=False
else:
 for i in range(2,r+1):
    if n%i==0:
       is_Prime=False
       break

if is_Prime:
   print(f"{n} is a prime number")
else:
   print(f"{n} is not a prime number")"""    

#SUM OF THE DIGITS OF A NUMBER
"""n = 1234
n_str= str(n)
n_len= len(n_str)
sum=0

print(f"Digits of the number are:")
while n > 0:
    digits = n%10
    print(digits)
    sum+=digits
    n//=10
print(f"Sum of the digits:{sum}")"""

#MAX OF 3 USER INPUTED NUMBER
"""n1= int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))

if n1>n2:
    if n1>n3:
        max=n1
    else:
        max=n3    
else:
    if n2>n3:
        max=n2
    else:
        max=n3  
print(f"Max is {max}")"""

#PRINTING FIRST N NUMBERS, CALCULATING THERE SUM, CALCULATING THE AVARAGE
"""sum=0
n=int(input("Enter the value of n:"))
print(f"First n numbers are:")
for i in range(0,n):
    print(i,end=" ")
    sum+=i
print()    
print(f"Sum of the first {n} numbers is:{sum}")    
avg=float(sum/n)
print(f"Average of the numbers is: {avg}")"""

#AREA OF A TRIANGLE
"""import math
s1= int(input("Enter first side of the 🔺 : "))
s2=int(input("Enter second side of the 🔺 : "))
s3=int(input("Enter third side of the 🔺 : "))

pr=float((s1+s2+s3)/2)

l=pr-s1
m=pr-s2
n=pr-s3

a=math.sqrt(pr*l*m*n)

print("Area of the triangle is ≈", round(a,3))"""

#ARRAY ELEMENTS ACCESSEING

#arr=[1,2,3,4,5]
#l=len(arr)

#print(l)

#1. Method 1\: Accessing the list elements in-order
 
#print("List elements in order:")
#for i in range(0,l,1):
    #print(arr[i])


#2. Method 2\: Accessing the list elements in-order

#print("List elements in order:")
#for i in range(0,l):
    #print(arr[i])


#Method Rev\: Accessing the list elemets in reverse order

#print("List elements in reverse order:")
#for i in range(l-1,-1,-1):
    #print(arr[i])

#Sum of the list elements

#sum=0
#print("Elements of the list are:")
#for i in range(0,l):
    #print(arr[i])
    #sum+=arr[i]
#print("Sum of the elements of the list is:", sum)        

#Average of the elements of the list

#sum=0
#print("Elements of the list are:")
#for i in range(0,l):
    #print(arr[i])
    #sum+=arr[i]
#print("Sum of the elements of the list is:", sum)     
#avg= float(sum/l)
#print("Average of the elements is:", round(avg,3))    

#SUM & AVERAGE OF THE ELEMENTS OF THE LIST {EASY METHOD:)}

#arr = [15, 20, 25, 10]

#print("Elements of the list are:")
#for x in arr:
    #print(x)

#total_sum = sum(arr)
#avg = total_sum / len(arr)

#print("Sum of the elements of the list is:", total_sum)
#print("Average of the elements is:", round(avg, 3))

#LINEAR SEARCH

#1.Method 1\: Traditional One

"""arr = [15, 20, 25, 10]
l=len(arr)

print("Elements of the list are:")
for x in arr:
    print(x)
item= int(input("Enter the item you are searching:"))

found=False

for i in range(0,l):
    if(item==arr[i]):
        found=True
        break
if found:
    print("Item found at index ", i)    
else:
    print("Item not found in the list")"""


#2.Method 2\: Using built-in enumerate()

"""arr = [15, 20, 25, 10]

print("Elements of the list are:")
for x in arr:
    print(x)

item = int(input("Enter the item you are searching: "))

for index, value in enumerate(arr):
    if value == item:
        print(f"Item found at position {index+1}")
        break
else:
    print("Item not found in the list")"""

#3.Method 3\: Using built-in in and .index()

"""arr = [15, 20, 25, 10]

print("Elements of the list are:")
for x in arr:
    print(x)

item = int(input("Enter the item you are searching: "))

if item in arr:
    ps=arr.index(item)+1
    print(f"Item found at position ",ps)
else:
    print("Item not found in the list")"""

#BINARY SEARCH

"""arr = [10,15,20,25]

l=len(arr)

print("Elements of the list are:")
for x in arr:
    print(x)

item = int(input("Enter the item you are searching: "))

lb=0
ub=l-1



found=False
while lb<=ub:
 mid=(lb+ub)//2
 if arr[mid]==item:
     found=True
     break
 elif item>arr[mid]:
   lb=mid+1
 else:
   ub=mid-1   
if found:
   print("Item foud at position ",mid+1)
else:   
   print("Item Not Found")"""

#USER INPUTED ITEMS FOR LIST

#1.Method 1\: Number of elements or items is known    

"""n=int(input("Enter the length of the list:"))
elems=[]

for i in range(n):
    item = input(f"Enter item {i + 1}: ")
    elems.append(item)
print("Your List is:",elems)"""

#2.Method 2\:
# For a list of strings
#items = input("Enter items separated by spaces: ").split()
#print("List:", items)

# For a list of numbers (integers)
#numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
#print("List of numbers:", numbers)