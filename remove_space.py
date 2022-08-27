# def remove_space(str1):
#     str1=str1.replace(' ','')
#     return str1
# print(remove_space('a b c d e'))



def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char
print(no_space('abc def'))