

def expanded_form(num):
    my_str = str(num)
    _length = len(my_str)
    j = 0
    res =''
    if _length == 1: return str(num)
    for item in my_str:
        _length -= 1
        if int(item) == 0: continue
        if j == 0:
            res += str(int(item) * pow(10,_length))
            j += 1
        else:
            res += '+'
            res += str(int(item) * pow(10,_length))
    return res
print(expanded_form(num=790))





