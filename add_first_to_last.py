def solution(a,b):
    c,d=a,b 
    
    if len (a)<len(b):
        return c+d+c
    elif len(a)>len(b):
        return d+c+d
print(solution('u', 'will'))