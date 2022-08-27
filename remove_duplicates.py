# input_list=[1,2,2,5,8,4,4,8]
# def remove_duplicates(duplist):
#     sqr_brk=[]
#     for element in duplist:
#         if element not in sqr_brk:
#             sqr_brk.append(element)
#     return sqr_brk
# print(remove_duplicates(input_list))


# list1=[1,2,3,[],4,[],5]
# i=0
# s=[]
# while i<len(list1):
#     if list1[i]!=[]:
#         s.append(list1[i])
#     i=i+1
# print(s)


# input_list=[1,2,2,5,8,4,4,8]
# i=0
# def remove_duplicates(duplist):
#     while i<len(input_list):
#         if input_list==2 or input_list==8 or input_list==4:
#             input_list.append(i)
#         i=i+1
#     print(input_list)
# a=[5,6,9,4]
# i=0
# while i<=0:
#     i=i+1
#     print(a[-1])
#     print(a[-2])
#     print(a[-3])
#     print(a[-4])
   
# a=[5,6,9,4]
# a.reverse()
# print(a)


# a=[5,6,9,4]
# i=1
# while i<=len(a):
#     print(a[-i])
#     i=i+1
# a=[5,6,9,4]
# for i in len(a):
#     print(a[-i])

# list1=[5,6,7,1]
# i=0
# sum=0
# while i<len(list1): 
#     sum=sum+list1[i]
#     i=i+1
# print(sum)

    
# list1=[5,6,7,1]
# sum=0
# for i in list1:
#     sum=sum+i
# print("sum is",sum)

# a=[5,6,7]
# b=[9,10,12]
# a.extend(b)
# print(a)
# a=[5,6,7]
# b=[9,10,12]
# i=0
# while i<=len(a):

# a=[2,3,2,4,5,6,9,6]
# i=0
# p=[]
# while i <len(a):
#     if (a [i]) not in p:
#         print(a[i])
        # i=i+1
# a=[2,3,2,4,5,6,9,6]
# i=0
# p=[]
# while i <len(a):
#     if (a [i]) not in p:
#         p.append(a[i])
#     i=i+1
# print(p)



# # Remove Duplicates from List

# dupList = []

# listNumber = int(input("enter no:-"))
# for i in range(1, listNumber + 1):
#     listValue = int(input("Enter the %d List Item = " %i))
#     dupList.append(listValue)

# print("List Items = ", dupList)

# uniqList = []

# for val in dupList:
#     if val not in uniqList:
#         uniqList.append(val)
   
# print("List Items after removing Duplicates = ", uniqList)

# Python Program to Remove Duplicates from List 2

# lit=[2,3,2,5,4,6]
# i=0
# while i<len(lit):
#     lit.pop(2)
#     i=i+1
#     print(lit)


lit=['a','b','a','c','e']
i=0
a=[]
while i<len(lit):
    if lit[i] not in a:
        a.append(lit[i])
    i=i+1

print(a)

# p=[9,4,6,1,8,9,1,3,4]
# i=0
# a=[]
# while i<len(p):
#         if (p[i])not in a:
#                 a.append(p[i])
#         i=i+1
# print(a)
        
# l=[9,8,6,0,9,6,7]
# i=0
# p=[]
# while i<(len(l)):
#         if (l[i]) not in p:
#                 p.append(l[i])
#         i=i+1
# print(p)