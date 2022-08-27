def kwargs(a,*b):
    c=a
    for i in b:
        c+=i
    print(c)
kwargs(1,2,3,4,5)