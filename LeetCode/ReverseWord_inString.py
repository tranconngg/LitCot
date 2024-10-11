def reverseWords(self, s):
        s=s.strip()
        list_s = s.split()
        return ' '.join(list_s[::-1])
# print(reverseWords("    hello world"))