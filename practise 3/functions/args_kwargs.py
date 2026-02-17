def names_func(*students): #if we don't know how many arguments will be here, we can use this parametr
    print("The smartest student is " + students[0]) #IT IS FOR TUPLE
names_func("Zhanelya", "Ali", "Maksat")

def func(**data): #we use double* when our argument is dictionary
    print(data["name"] + ", her age " + data["age"]) #IT IS FOR DICT
func(name = "Milana", age = "18")

def union(name, *education, **other): #seguence: 1-regular parametres, 2-*args, 3-**kwards
    print("Name: ", name)
    print("Education: ", education)
    print("Other:, ", other)
union("Milana", "Average", "Higher", age = 30, city = "Almaty")

def function(a, b, c): #we use *args to unpack lists 
    return a + b + c
number = [5, 10, 15]
result = function(*number)
print(result)

def fun(name, surname): #we use **kwards to unpack dict(dict - > named arguments)
    print("Hello,", name, surname)
person = {"name": "Zhanelya", "surname": "Ermek"}
fun(**person)

    
