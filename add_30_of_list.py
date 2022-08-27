def num():
    a=[11,23,19,7,12,18,34]
    b=30
    i=0
    c=[]
    while i<len(a):
        j=0
        d=[]
        while j<len(a):
            if a[i]+a[j]==b and a[j]>a[i]:
                d.append(a[i])
                d.append(a[j])
                c.append(d)
            j=j+1
        i=i+1
    print(c)
num()
