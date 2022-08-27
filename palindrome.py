def is_palindrome(s):
    left=0
    right=len(s)-1
    while right>=left:
        if not s[right]==s[left]:
            return False
        left+=1
        right-=1
    return True
print(is_palindrome("aba"))