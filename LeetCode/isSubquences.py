def isSubsequence(s, t):
    i,j =0,0
    while j < len(s) and i < len(t):
            if (s[j]==t[i]):
                j+=1
            i+=1
    return j == len(s)
print(isSubsequence("mess","Leo messi"))