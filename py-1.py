# print ('hello test')
# print ('hello test combining next variable', end="-")
from asyncio.windows_events import NULL


age = 23
age = 25;
name = 'sarmad'
# print('age of ',name, 'is ', age)
# print('variable of age is ',age)


patient_name = 'John Smith'
patient_age = 20
patient_type = 'New'

# print(patient_name, ' is ', patient_type , ' patient having age of ', patient_age, ' years old')


# INPUTS

# input_name = input('Enter your name? ')
# print('Hello '+ input_name)

#type conversions
#input function always returns string
# birth_year = input('Enter birth year: ')
# age  = 2022-int(birth_year)

# print('Hello ', name , 'Your age is ',age)

#basic calculator

# english = float(input('Enter Marks of English: '))
# math = float(input('Enter marks of Math: '))
# computer = float(input('Enter marks of Computer: '))

# obtained = float(english+math+computer)
# total = 300

# print('You got ', obtained ,' marks out of ', total)

#STRINGS

course = 'This is python course';
#: course[:] copies all the string
#: course[5:] copies all the string starts from index 5
# print(course.find(' is ')) # find returns index from string starts from 0;

# print(course.replace('is', 'us'))

# print('cour' in course)   # finds char in string and retruns true


#OPERATORS

# + addition, - subtraction, * multiplication, / division (returns float), // division returns int, % returns reminder, ** exponent returns power of num
# augmented / enhanced assignment operator (x = 10, x = x+3, x+=3)
#   membership operators (in / not in)
#   identity operators ( is / not is )

# x = 10
# x+= x+3
# print(x)

x = 10 + (2 * 3) / 2
y = 1.5 * 12
# print(x)
# print(y)


# print('' == NULL)
#logical operators (and or not)
# print(not 5 > 10)

# temprature = 15

# if temprature > 30:
#     print("Its hot day")
#     print('kepp drinking water')

# elif temprature > 20:
#     print('Its nice day')
    
# elif temprature < 20:
#     print('Its cold day')
#     print('Be inside house')

# else:
#     print('Its snow fall')
# print('Good Luck')


#weight calculator

# weight = int(input('Enter your weight: '))
# weight_type = input('K(g)s or L(bs)?')

# 1kg = 2.2lb
# 1lb = 0.45kg

# if weight_type.upper() == 'L':
    # if weight_type == 'L' or weight_type == 'l':
    # weight = weight*2.2
    # print('Weight in KGs ', weight)

# if weight_type.upper() == 'K':
#     weight = weight*0.45
#     print('Weight in Lbs ', weight)
    
name = 'Jennifer'
city = 'UAE'
# print(name[1:-1])

another_name = name[:]
print(another_name)
# new_name = '{name} is from  {city}'
# print({new_name})

i = 10
while i > 1:
    # print(i)
    i = i-1
    # print(i*'*')
    # i = i+1
    
    #LISTS
names = ['abc', 'xyz', 'mno', 'pqr']
print(names[-4])
# names[0] = 'test'
# print(names)

# print(names[0:3])   # starts from 0, but before index of 3

numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)

numbers.insert(7, names)
# print(numbers[7])

print(3 in numbers)

# print(len(numbers))

for item in numbers:
    print(item)
    
nums = range(1, 99, 2)

#prints numbers starts from 1 to 99 skipping 2 nums

for num in nums:
    print(num)
    
#TUPLES
#connected lists, can not be changed
#tuples can not be appended/inserted/removed
tup = (1,2,3)
print(tup)
print(tup.count('2'))
#count returns number of occurances of given number


# price of house 1M, if buyer has good credit
# they put 10% of down payment
#else put 20% of down payment

good_credit = False
house_price = 1000000
if good_credit:
    down_payment = house_price*10/100
else:
    down_payment = house_price*20/100

print(down_payment)