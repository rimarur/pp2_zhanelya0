def ftoc(fah): #function to convert from fahrengeith to celsius
  return (fah - 32) * 5 / 9
print(ftoc(77))

def get_greeting():
  return "KBTU, hi!"
print(get_greeting())

def get_greeting1():
  return "KBTU, hi!"
message = get_greeting1()
print(message)

def my_function2():
  pass

def greet(name): #docstring - краткое описание функции
    """This function greets a person by name."""
    print("Hello", name)
print(greet.__doc__) #to see coment