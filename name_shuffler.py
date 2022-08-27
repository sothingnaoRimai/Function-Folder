def name_shuffler(str):
    sp=str.find(' ')
    return str[sp+1:]+' '+str[:sp]

# def name(s):
#     sp=s.split()
#     return sp[1]+' '+sp[0]
# print(name('Somila Rimai'))