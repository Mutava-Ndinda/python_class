def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
         print(number)

def odd_or_even(m):
   nums = range(m)
   for num in nums:
      if num%2 ==0:
         print(f"{num} is even")
      else:
         print(f"{num} is odd")

def check_divisibility(j):
   numbs = range(j)
   for numb in numbs:
      if numb%2 == 0:
         print(f"{numb} is divisible by 2")
      elif numb%3 ==0:
         print(f"{numb} is divisible by 3")
      elif numb%5 ==0:
         print(f"{numb}is divisible by 5")
      elif numb%7 == 0:
         print(f"{numb} is divisible by 7")
      else:
         print(f"{numb} is not divisible by 2,3,5 and 7")

def countdown(v):
   while v>0:
      print(v)
      v-=1

def countdown_five(y):
   while y>0:
      print(y)
      if y==5:
        break
      y-=1

def divisible_by7(f):
   x=1
   while x<f:
      x+=1
      if x%7 !=0:
         continue
      print(x)


def fizzbuzz(n):
   nums =range(n)
   for num in nums:
      if num%3 ==0:
         print(f"{num} is Fizz")
      elif num%5 ==0:
         print(f"{num} isBuzz")
      else:
         print(f"{num} is FizzBuzz")


def print_nums():
   l=0
   while l<50:
      l+=1
      if l%2 !=0:
         continue
      print(l)
      