# Write a program to sort a dictionary in ascending or descending according to 
# its values .
# Input :-
# Code Example


# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}
# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

# l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for x in l:
#     for k in l:
#         if l[x]<l[k]:

#             l[x],l[k]=l[k],l[x]
#         else: 
#             l[k],l[x]=l[x],l[k]
# print(l)


# l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for x in l:
#     for k in l:
#         if l[x]<l[k]:

#             l[x],l[k]=l[k],l[x]
#         if l[k]<l[x]:
#             l[k],l[x]=l[x],l[k]
# print(l)

# # Ascending
# l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50,"koney":9000}
# for x in l:
#     for k in l:
#         if l[k]<l[x]:
#             l[k],l[x]=l[x],l[k]
#         if l[x]<l[k]:

#             l[x],l[k]=l[k],l[x]
# print(l)


# # Descending
# l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50,"koney":9000}
# for x in l:
#     for k in l:
#         if l[x]<l[k]:
#             l[x],l[k]=l[k],l[x]
#         if l[k]<l[x]:
#             l[x],l[k]=l[k],l[x]
# print(l)