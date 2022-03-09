'''
 lab6 
'''
 
 #3.1
 
for i in range(6):
     if i !=3:
         print(i)


#3.2 what does result = 1 mean? what's that line's function

result = 1

for i in range(1,6):
    result = result *i
print(result)


#3.3
result = 0

for i in range(1,6):
    result = result +i
print(result)


#3.4 whys this work... WHAT DOES RESULT = MEAN
result = 8

for i in range(3,8):
    result = result *i
print(result)


#3.4
result = 1

for i in range(3,9):
    result = result *i
print(result)

#3.5..... precanceled out, how to do it all on here instead?
result = 1
for i in range (4,9):
    result = result * i
print(result)

#3.6 
result = 0 
for word in "this is my 6th string".split():
    print(word)
    result = result + 1

print(result)