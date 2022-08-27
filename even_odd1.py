
def num(n):
    i=1
    b=[]
    while i<=n:
        a=i
        b.append(a)
        i=i+1
    return b
def even_odd(b):
    i=0
    while i<len(b):
        if b[i]%2==0 :
            print(b[i],"is even")
        elif b[i]%2!=0:
            print(b[i],"is odd")
        i=i+1
n=int(input("enter no: "))
print(num(n))
even_odd(num(n))

    