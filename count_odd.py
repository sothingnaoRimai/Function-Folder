def odd_count(n):
    c=0
    i=0
    while i<n:
        if i%2==1:
            c=c+1
        i=i+1
    return c
print(odd_count(15))