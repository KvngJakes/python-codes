'''
for i in [11,10,9,8,7,6,5,4,3,2,1]:
    if i != 0:
        i -= 1
        print(i)
    
print("Time's Up")

###############################

total = 0

while total < 100:
    print(total)
    total += 1

print(f' total sum is {total}.')

###############################

number = int(input('Enter a number for muplitication table: '))
limit = int(input('enter how many multiple you want: '))

print(f"\nMulplication Table for {number}:")
for i in range(1, limit + 1):
    print(f"{number} * {i} = {number * i}")

###############################

for i in range(1,6):
    
    print("*" * i)

print("REVERSE")
star = 5
while star > 0:
     print("*" * star)
     star -= 1

###############################

def greeting(name):
    print("Hello, {}! Welcome back.".format(name))
greeting("Jakes")
greeting("AYO")
greeting("Dammy")

###############################

def total():
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    sum = num1 + num2
    return(sum)
sum_total = total()
print(sum_total)

###############################

def numbers():
    num4 = int(input("enter a number: "))
    if num4 % 2 == 0:
        print("EVEN NUMBER")
    else:
        print("ODD NUMBER")
numbers()

###############################

def squared(number):
  
   return number ** 2

for num in range(1,11):
    result = squared(num)
    print(result)


#########################

word = "Hi"
num = 5

def repeat(word, num):
    
    for i in range(num):
        print(word)
        
repeat("hello", 3)


###################################

def find_largest(numbers):
    largest = numbers [0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
list = [2, 3, 7, 9, 8]
result = find_largest(list)
print(result)

##########


def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
word ="HellouAIi"
result = count_vowels(word)
print(result)


#########################

'''

def pass_checker():
    user_pass = input("Enter a password")
    things = ['!', '@', '$', '#', '*', '&']
    if len(user_pass) >= 8 and {user_pass} == things:
        print("PASSWORD IS STRONG")
    else:
        print("TOO SHORT")
    return pass_checker()
password = pass_checker()
print(password)
    


