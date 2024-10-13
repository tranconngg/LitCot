def uniqueOccurrences(arr):
        dict_arr={}
        for i in range(len(arr)):
            if arr[i] not in dict_arr:
                  dict_arr[arr[i]]=1
            else:
                keyy=dict_arr.get(arr[i])
                keyy +=1
                dict_arr[arr[i]]=keyy

        val_unique = dict_arr.values()
        n = len(val_unique)
        return n == len(set(val_unique))
print(uniqueOccurrences([1,2]))