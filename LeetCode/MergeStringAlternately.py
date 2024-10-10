def mergeAlternately(word1, word2):
        min_length = min(len(word1),len(word2))
        merge =''
        for i in range(0,min_length):
            merge += word1[i]
            merge += word2[i]
        merge +=word1[min_length:]
        merge +=word2[min_length:]
        return merge
print(mergeAlternately("abc","xyz"))