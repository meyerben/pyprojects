def FizzBuzz():
    list = []
    for i in range(1,101):
        if (i % 5 == 0) and (i % 3 == 0):
            list.append("FizzBuzz")        
        elif i % 5 == 0:
            list.append("Buzz")
        elif i % 3 == 0:
            list.append("Fizz")
        else:
            list.append(i)
    print list

#FizzBuzz()

print 4.5//2