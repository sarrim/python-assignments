    #   Count the total number of ‘m’ in a given string

str = "mariyaa mennen"

print(reversed(str))
pass



count = 0
for m in str:
    # print(m)
    if(m != 'm'):
        continue;
    if(m == 'm'):
        count = count + 1
        # print(count)

else:
    print('Counting of number is done')
    print('total number of letter "m" in ', str ,' is/are ', count)
    

    #   reverse loop

list = [1,2,3,4,5,6,7,8,9,0]

num = 15

for i in reversed(list):
    print(i)

print('\n')

for j in range(num,-1,-1):
    print(j)