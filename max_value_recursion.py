def max_rec(list,n):
    if n==0:
        return list[n]
    return max(list[n-1]),max_rec(list,n-1)
list=[4,3,1,5]
a=max_rec(list,n=len(list))
print(a)