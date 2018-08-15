numbers=list()
while True:
    inp=input('enter a number')
    if (inp=='done'):
        break
    numbers.append(inp)
print (numbers)
print ('maximum:',max(numbers))
print ('minimum:',min(numbers))
