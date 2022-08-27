def lar_sma():
    e=[8,900,42,89,4567]
    i=0
    largest=e[0]
    smallest=e[0]
    while i<len(e):
        if e[i]>largest:
            largest=e[i]
        elif e[i]<smallest:
            smallest=e[i]
        
        i=i+1
    print(largest)
    print(smallest)
lar_sma()

