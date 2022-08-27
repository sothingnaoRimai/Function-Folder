
def smash(words):
    i=0
    s=""
    while i<len(words):
        s=s+words[i]
        s=s+" "
        i=i+1
    return s
    # if s:
    #     return "'"+s+"'"
print(smash(["this", "is", "a", "really", "long", "sentence"]))


