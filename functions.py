# we use def keyword

# def hello_func(greeting,name='you'):
#     return('{} ,{}'.format(greeting,name))

# print(hello_func('Hi',name='bakari')   ) 

# def greeting(name):
#     return(f"hello,{name}")
    
# print(greeting("bakari"))    

def  greet_programmer():
    return("Hello, programmer!")
print(greet_programmer())

def greet(name):
    return(f"Hello ,{name}")
print(greet('bakari'))

def greet_with_default(name='juma'):
    return(f"Hello,{name}")
print(greet_with_default())

def add(a,b):
    return(a+b)
print(add(3,2))

def halve(a):
    return(a/2)
print(halve(10))