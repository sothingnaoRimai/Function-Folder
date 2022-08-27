def find_sum(sum):
    if sum==0:
        return 0
    print(sum)
    return sum+find_sum(sum-1)
print(find_sum(5))

