def  prime():
    a=int(input("enter no: "))
    i=0
    b=[]
    while i<a:
        def num1():
            j=2
            sum=0
            while j<i:
                if i%j==0:
                    sum+=1
                j=j+1
            if sum==0:
                b.append(i)
        i=i+1
        num1()
    print(b)
prime()
