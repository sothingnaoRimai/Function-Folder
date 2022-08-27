
def add(x,y):
    c=x+y
    print(c) 

def subs(x,y):
    d=x-y
    print(d) 

def mul(x,y):
    f=x*y
    print(f)

def calculator(x,y,op):
    
    if op=="+":
        add(x,y)
    elif op=="-":
        subs(x,y)
    elif op=="*":
        mul(x,y)
    
x=int(input("enter no"))
y=int(input("enter no"))
op=input("enter operator")
calculator(x,y,op)