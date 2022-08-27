
# reverse the string

str = 'sarmadsoomro'

for i in reversed(str):
    print(i, end="")

    #   nested loop

list = [1,2,3,4,5]

for i in list:
    print(1*i)
    # print('\n')
    for j in range(1,5):
        print(i*j)


    #   Nested for loop to print the pattern


for i in range(1,6):
    print('*', end="\n")
    for j in range(1,6):
        print()
    
