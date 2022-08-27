a=[1,2,3,4,5,6,7]
b=[2,4,5,7,8,9,0]
def not_in():
    i=0
    j=[]
    while i<len(a):
        if a[i] not in b:
            j.append(a[i])
        i=i+1
    print(j)
not_in()