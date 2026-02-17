x = lambda a : a + 10 #lambda arguments: expression
print(x(5))

add10 = lambda a: a + 10
print(add10(5))  # 15

multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

lol = lambda a, b: a*b
print(lol(3,4))