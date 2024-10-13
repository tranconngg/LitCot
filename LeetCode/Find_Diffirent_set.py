def findDifference(nums1, nums2):
        set_s1=set(nums1)
        set_s2=set(nums2)
        return [list(set_s1-set_s2),list(set_s2-set_s1)]
print(findDifference([1,2,3,3],[1,1,2,2]))