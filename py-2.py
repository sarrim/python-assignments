
from base64 import encode


txt = "We are the so-called \"Vikings\" from the north."

name = 'sarmad'
age = 27

sentence = 'my name is '+ name + ' having age of {}'
print(txt)

print(sentence.format(age))

print(name.encode())