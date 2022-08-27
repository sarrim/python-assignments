#some strings in quotes

print('some text')

print("some text doesn\t show")

print('some text doesn\'t show')

print('some \name')
print(r'some \name')


prefix = 'py'

print(prefix+'thon')
var = 2*prefix+'thon'
print(var)
print(var[2:])  # extracts characters from string character index 2
print(var[:2])  # extracts character from index 0 to 2 (2 excluded)

print(var[:2] + var[2:])

str = 'this is test string'

print(str[2::-1])

# for i in str:
#     print(i)

sum = 0;

for num in range(0,10):
    sum = num**num;
    print(sum , ' num:', num)
    

    

