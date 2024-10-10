from math import gcd
def gcdOfStrings(str1, str2):
        if str1 + str2 != str2 + str1:
            return ''
        n = gcd(len(str1), len(str2))
        return str1[:n]
print(gcdOfStrings("ABC","ABCABC"))
print(gcdOfStrings("ABABAB","ABAB"))