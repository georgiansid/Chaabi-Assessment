x = lambda num : 1 if num <= 1 else num*(x(num-1))
number = 5
print(x(number))