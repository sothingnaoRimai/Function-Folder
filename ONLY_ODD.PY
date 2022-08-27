
def num():
    p=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i=0
    c=[]
    while i<len(p):  
        if (p[i]%2!=0):
            c.append(p[i])
        i=i+1
    print(c)
num()