def sq(a, b):
    return a*a + b*b
print(sq(2, 3))

def func():
    return["SITE", "SEPI", 'SCE']
schools = func()
print(schools[1])

def myfn(name, /): #we use "/" if our arguments positional-only
    print("Hello", name)
myfn("Zhanelya")   

def my_function(*, name): #we use "*" before argument if there are keyword-only argument
  print("Hello", name)
my_function(name = "Zhanelya")

def fnc(a, b, /, *, c, d): #Arguments before / are positional-only, and arguments after * are keyword-only
  return a + b + c + d
result = fnc(5, 10, c = 15, d = 20)
print(result)
