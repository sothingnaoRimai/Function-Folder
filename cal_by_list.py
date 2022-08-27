def mul(op):
    a=[90,80,60,50]
    b=[30,49,59,60]
    i=0
    while i <len(a):
        if op=="+":
            print(a[i]+b[i],end=" ")
        elif op=="-":
            print(a[i]-b[i],end=" ")
        elif op=="*":
            print(a[i]*b[i],end=" ")
        i=i+1
op=input("enter no: ")
mul(op)