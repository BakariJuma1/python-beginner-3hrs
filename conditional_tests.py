def admin_login(username,password):
    if username=='admin' and password=='123445':
        return('access granted')
    else:
        return("access denied")
    
print(admin_login('admin','12345'))    


def hows_the_weather(temperature):
    if temperature<40:
        return("its brisk out their")
    elif temperature<=65:
        return("its a little chilly ")
    elif temperature>85:
        return("its dong too hot")
    else:
        return("its perfect out their ")
print(hows_the_weather(44))    

def calculator(a,b,operation):
    if operation=='+':
        return(a+b)
    elif operation=='-':
        return(a-b)
    else:
        print("invalid operation")
print(calculator(4,5,"-"))        