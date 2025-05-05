# scope of name is global
name='joe'
def greeting():
    return(f"hello,{name}")
print(greeting())
# use global keyword to modify global variables in a functio though its discourage d as it make s debugging hard
