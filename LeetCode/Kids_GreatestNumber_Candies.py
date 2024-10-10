def kidsWithCandies(candies, extraCandies):
    max_candi= max(candies)
    list_check=[]
    for can in range(len(candies)):
        if candies[can]+extraCandies >= max_candi:
            list_check.append(True)
        else:
            list_check.append(False)
    return list_check
print(kidsWithCandies([1,4,2,6,5,4],3))
