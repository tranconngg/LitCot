def maxVowels(s, k):
        left, right = 0,0
        max_vowels = 0
        cnt = 0
        vowels = ['u','e','o','a','i']
        while right < len(s):
                if s[right] in vowels:
                        cnt +=1
                if right - left +1 == k:
                        if cnt > max_vowels:
                                max_vowels = cnt
                        if s[left] in vowels:
                                cnt -=1
                        left +=1

                right +=1
        return max_vowels
print(maxVowels("aeiou",2))