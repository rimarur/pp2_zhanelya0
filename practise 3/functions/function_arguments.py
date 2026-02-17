def func(user = "guest"): #if we don't add parametr to func => it will write this argument
    print("Hello, " + user)
func("Zhanelya")
func()

def function(name, age):
    print("My name is "+ name)
    print("I am " + name + " and I am " + age)
function("Zhanelya", "18")

def fn(schools): #LIST
    for sc in schools:
        print(sc)
my_schools = ["SITE", "SEPI", "SCE"]
fn(my_schools)

def myfn(data): #DICT
    print("School", data["school"])
    print("Year", data["year"])
my_data = {"name": "Zhanel", "school": "SITE", "year": "2025"}
myfn(my_data)