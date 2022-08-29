def myFunction():
    # print('test func')
    # num = '10'
    for i in range(1,11):
        if(i%2 == 0):
            continue;
        print(i)


myFunction()

myList = ["apple", "banana", "cherry", "kiwi", "mango"]
myList2 = ["apple", "banana", "cherry", "kiwi", "mango"]
myList3 = [1,3,5,7,9]
myList.sort(reverse=True)
print(myList)
newList = []
for x in myList:
    if 'i' in x:
        print(x)
        newList.append(x)

yourList = myList.copy()

print('your list ', yourList)

myList.extend(myList2)
print(myList+myList2+myList3)