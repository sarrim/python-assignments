#   calculate average from the list

numbers = [10,20,30,40,50]

total = 0
count = 0
for avg in numbers:
    total+= avg
    count = count+1
        
average = total / count
print('average of above list is: ',average)


#   print even and odd numbers from list

list = range(1,10)

for i in list:
    # print(i)
    if i%2 == 0:
        print(i, ' is even number')
    elif i%2 == 1:
        print(i, ' is odd number')